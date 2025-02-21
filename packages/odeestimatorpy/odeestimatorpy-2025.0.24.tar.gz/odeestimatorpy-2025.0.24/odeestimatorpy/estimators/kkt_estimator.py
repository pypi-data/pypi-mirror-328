import numpy as np
import sympy

from scipy.linalg import block_diag
from sympy import Eq, lambdify, Mul
from sympy.stats import independent

from odeestimatorpy.estimators.estimator import AbstractODEEstimator
from odeestimatorpy.models.linear_ode_model import LinearODEModel


class KKTLinearODEParameterEstimator(AbstractODEEstimator):
    def __init__(self, model: LinearODEModel, ode_results: np.ndarray, solver=np.linalg.solve):
        """
        Initialize the solver for a linear ordinary differential equation system.

        Args:
            model (LinearODEModel): Ordinary differential equation system linear in the parameters
            ode_results (numpy.ndarray): Data matrix without noise (rows: points, columns: variables)
            solver: (callable, optional): Solver to use. Defaults to np.linalg.solve
        """

        super().__init__(model, ode_results)

        self.solver = solver

        self.number_of_constraints = len(model.constraints)
        self.number_of_parameters = len(model.parameter_names)
        self.input_values = [model.inputs[name] for name in sorted(model.inputs.keys())]

        self.index_by_parameter = {}
        self.independent_terms_by_equation = []

        self.callables_per_equation = [self._extract_callables(equation) for equation in self.model.equations]

    def _extract_callables(self, expr):
        """
        Given a sympy expression, returns a list of functions
        independent for each term multiplied by a parameter.

        Args:
            expr (sympy.Expr): The symbolic expression.

        Returns:
            list: List of independent callable functions.
        """
        # Ensure the expression is fully expanded
        expr = expr.expand()

        # Extract the terms of the expression
        terms = expr.as_ordered_terms()

        # List to store the callables
        callables = []

        independent_terms = []

        # Iterate over the terms
        for term in terms:
            # Check if the term contains a parameter
            for param in self.model.parameter_symbols:
                if param in term.free_symbols:
                    factor = term / param
                    callables.append(lambdify([self.model.independent_variable] + self.model.variable_symbols,
                                              factor, modules=["numpy"]))
                    if param in self.index_by_parameter:
                        raise ValueError(f"Parameter {param} already used in another equation")
                    self.index_by_parameter[param.name] = len(self.index_by_parameter)
                    break
            else:
                # If no parameter is found, store it as an independent term
                independent_terms.append(term)

        independent_terms = [lambdify([self.model.independent_variable] + self.model.variable_symbols + self.model.inputs_symbols, expr) for expr in independent_terms]
        # Store independent terms as a sum for later evaluation
        self.independent_terms_by_equation.append(lambda *args: 0 if len(independent_terms) == 0 else sum(f(*args) for f in independent_terms))

        return callables

    @staticmethod
    def _compute_weighted_derivative(col, f, h, input_values, data):
        """
        Computes a weighted sum of function values evaluated over a dataset D
        where the weights are derived from the finite differences of the dataset.

        Args:
            col (int): The column index used to compute the finite differences (slope).
            f (callable): The function to evaluate.
            h (callable): The independent terms.
            input_values(list): The values for the model inputs
            data (ndarray): Dataset of tuples, each containing values corresponding to the columns.

        Returns:
            float: The weighted sum of function values.
        """
        slopes = np.diff(data[:, col]) / np.diff(data[:, 0])
        h_values = np.array([h(*row, *input_values) for row in data[:-1]])
        adjusted_slopes = slopes - h_values

        f_values = np.array([f(*row) for row in data[:-1]])
        return np.sum(f_values * adjusted_slopes)

    @staticmethod
    def _scalar_product(f, g, data):
        """
        Computes the scalar product of two functions over a dataset D using numpy.dot.

        Args:
            f (callable): The first function.
            g (callable): The second function.
            data (ndarray): An array of tuples representing the dataset. Each tuple contains input values.

        Returns:
            float: The scalar product result.
        """
        # Evaluate f and g over the dataset D
        f_values = np.array([f(*data_point) for data_point in data])
        g_values = np.array([g(*data_point) for data_point in data])

        # Use numpy.dot to compute the scalar product
        return np.dot(f_values, g_values)

    @staticmethod
    def _compute_normal_matrix(basis_functions, data):
        """
        Construct the normal matrix associated with a specific equation.

        Args:
            basis_functions (list[Callable]): List of basis functions for the equation.
            data (ndarray): An array of tuples representing the dataset. Each tuple contains input values.

        Returns:
            numpy.ndarray: Normal matrix N_fi.
        """

        number_of_parameters = len(basis_functions)
        normal_matrix = np.zeros((number_of_parameters, number_of_parameters))
        for j in range(number_of_parameters):
            for k in range(number_of_parameters):
                scalar_product = KKTLinearODEParameterEstimator._scalar_product(basis_functions[j], basis_functions[k],
                                                                                data)
                normal_matrix[j, k] = normal_matrix[k, j] = scalar_product

        return normal_matrix

    def _build_constraints(self):
        """
        Build the rij and cij vectors for equality constraints.

        Ensures all constraints are of the form x = y.
        Raises an exception if not.

        Returns:
            tuple: (dict, dict)
                - r_vectors: Dictionary of rij row vectors.
                - c_vectors: Dictionary of cij column vectors.
        """
        r_vectors = {}
        c_vectors = {}

        for constraint in self.model.constraints:
            # Ensure the constraint is an equality constraint
            if not isinstance(constraint, Eq):
                raise ValueError(f"Constraint {constraint} is not an equality constraint of the form ax == by.")

            # Extract left-hand side and right-hand side
            lhs = constraint.lhs
            rhs = constraint.rhs

            # Extract coefficient and symbol for lhs
            if isinstance(lhs, Mul) and len(lhs.args) == 2 and lhs.args[0].is_Number:
                lhs_coefficient, lhs_symbol = lhs.args[0].evalf(), lhs.args[1]
            else:
                lhs_coefficient, lhs_symbol = 1, lhs

            # Extract coefficient and symbol for rhs
            if isinstance(rhs, Mul) and len(rhs.args) == 2 and rhs.args[0].is_Number:
                rhs_coefficient, rhs_symbol = rhs.args[0].evalf(), rhs.args[1]
            else:
                rhs_coefficient, rhs_symbol = 1, rhs

            # Ensure both lhs and rhs are valid parameters
            if lhs_symbol.name not in self.model.parameter_names or rhs_symbol.name not in self.model.parameter_names:
                raise ValueError(f"Both sides of the constraint {constraint} must be valid parameter names.")

            # Get the indices of the parameters
            i = self.index_by_parameter.get(lhs_symbol.name, -1)
            j = self.index_by_parameter.get(rhs_symbol.name, -1)

            if i == -1 or j == -1:
                ValueError(f"Parameter in constraint {constraint} is not used in equations")

            # Build rij and cij vectors
            ri = np.zeros(self.number_of_parameters)
            ri[i] = lhs_coefficient
            ri[j] = -rhs_coefficient

            r_vectors[(i, j)] = ri
            c_vectors[(i, j)] = ri.T

        return r_vectors, c_vectors

    def _build_system_matrix(self, normal_matrices, r_vectors, c_vectors):
        """
        Construct the system matrix A by combining normal matrices and constraints.

        Args:
            normal_matrices (list[numpy.ndarray]): List of normal matrices for each equation.
            r_vectors (dict[Tuple[int, int], numpy.ndarray]): List of rij row vectors.
            c_vectors (dict[Tuple[int, int], numpy.ndarray]): List of cij column vectors.

        Returns:
            numpy.ndarray: System matrix A.
        """
        blocks = normal_matrices + [
            np.zeros((self.number_of_constraints, self.number_of_constraints))
        ]

        a = block_diag(*blocks)

        # Start placing rij rows and cij columns in the corresponding positions
        index = a.shape[0] - self.number_of_constraints

        for (i, j), rij in r_vectors.items():
            a[index, :rij.shape[0]] = rij.flatten()

            cij = c_vectors[(i, j)]
            a[:cij.shape[0], index] = cij.flatten()  # Place the cij vector in the column

            index += 1

        return a

    def _build_rhs_vector(self, size):
        """
        Build the right-hand side vector b for the system AX = b, combining
        scalar products of the functions in the system and their derivatives.

        Returns:
            numpy.ndarray: The right-hand side vector b.
        """
        # Initialize the vector b with zeros
        b = np.zeros(size)

        row = 0
        # Iterate through the equations in the system
        for i, callables in enumerate(self.callables_per_equation):
            # Iterate through the parameters in each equation
            independent_term = self.independent_terms_by_equation[i]
            for basic_function in callables:
                # Compute the scalar product derivative and accumulate it in b
                b[row] += self._compute_weighted_derivative(i + 1, basic_function, independent_term, self.input_values, self.ode_results)
                row += 1

        return b

    def solve(self):
        """
        Solve the linear system of equations AX = b.

        Returns:
            numpy.ndarray: Estimated parameters vector.
        """
        # Build normal matrices
        normal_matrices = []
        for basis_functions in self.callables_per_equation:
            normal_matrix = self._compute_normal_matrix(basis_functions, self.ode_results)
            normal_matrices.append(normal_matrix)

        # Build constraints
        r_vectors, c_vectors = self._build_constraints()

        # Build the system matrix A and the vector b
        a = self._build_system_matrix(normal_matrices, r_vectors, c_vectors)
        b = self._build_rhs_vector(np.shape(a)[1])

        # Solve the system
        try:
            solution = self.solver(a, b)
        except Exception as e:
            #raise ValueError(f"Error solving the system with solver {self.solver.__name__}. "
                            # f"Exception: {str(e)}") from e
            return {name: str(e) for name in self.model.parameter_names}

        estimated_parameters = { self.model.parameter_names[i]: float(value) for i, value in enumerate(solution[:self.number_of_parameters])}
        self.model.set_parameters(estimated_parameters, [])

        return estimated_parameters