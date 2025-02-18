from typing import Union, Callable
import numpy as np
from .layers import Layer
import matplotlib.pyplot as plt
from .utils import get_rotation_matrix

class MoireLattice:
    def __init__(
        self,
        latticetype:Layer,
        a:int, b:int,
        nx:int=1, ny:int=1,
        pbc:bool=True,
        k:int=1,  # number of orbitals
    ):
        # study_proximity = 1 means only studying nearest neighbours will be enabled,
        # 2 means study of next nearest neighbours will be enabled too and so on,
        # always better to keep this value 1 or two more than what you will actually need.
        lower_lattice = latticetype(pbc=pbc)
        upper_lattice = latticetype(pbc=pbc)

        lv1, lv2 = lower_lattice.lv1, lower_lattice.lv2

        # c = cos(theta) between lv1 and lv2
        c = np.dot(lv1, lv2) / (np.linalg.norm(lv1) * np.linalg.norm(lv2))
        beta = np.arccos(c)
        mlv1 = lv1 * a + lv2 * b
        mlv2 = get_rotation_matrix(beta).dot(mlv1)
        
        # the actual theta is the angle between a*lv1 + b*lv2 and b*lv1 + a*lv2
        one = a * lv1 + b * lv2
        two = b * lv1 + a * lv2
        c = np.dot(one, two) / (np.linalg.norm(one) * np.linalg.norm(two))
        theta = np.arccos(c)  # in radians
        print(f"theta = {theta:.4f} rad ({np.rad2deg(theta):.4f} deg)")

        upper_lattice.perform_rotation(theta)

        lower_lattice.generate_points(mlv1, mlv2, nx, ny)
        # return
        upper_lattice.generate_points(mlv1, mlv2, nx, ny)

        self.a = a
        self.b = b
        self.nx = nx
        self.ny = ny
        self.lower_lattice = lower_lattice
        self.upper_lattice = upper_lattice
        self.theta = theta
        self.mlv1 = mlv1
        self.mlv2 = mlv2
        self.orbitals = k
        self.ham = None

        print(f"{len(self.lower_lattice.points)} points in lower lattice")
        print(f"{len(self.upper_lattice.points)} points in upper lattice")

        # self.plot_lattice()

    def plot_lattice(self):
        mlv1 = self.mlv1
        mlv2 = self.mlv2
        nx = self.nx
        ny = self.ny

        # plt.plot(*zip(*self.lower_lattice.points), 'r.', markersize=2)
        # plt.plot(*zip(*self.upper_lattice.points), 'b.', markersize=2)
        self.lower_lattice.plot_lattice(colours=["b"], plot_connections=True)
        self.upper_lattice.plot_lattice(colours=["r"], plot_connections=True)

        # parallellogram around the whole lattice
        plt.plot([0, nx*mlv1[0]], [0, nx*mlv1[1]], 'k', linewidth=1)
        plt.plot([0, ny*mlv2[0]], [0, ny*mlv2[1]], 'k', linewidth=1)
        plt.plot([nx*mlv1[0], nx*mlv1[0] + ny*mlv2[0]], [nx*mlv1[1], nx*mlv1[1] + ny*mlv2[1]], 'k', linewidth=1)
        plt.plot([ny*mlv2[0], nx*mlv1[0] + ny*mlv2[0]], [ny*mlv2[1], nx*mlv1[1] + ny*mlv2[1]], 'k', linewidth=1)

        # just plot mlv1 and mlv2 parallellogram
        plt.plot([0, mlv1[0]], [0, mlv1[1]], 'k', linewidth=1)
        plt.plot([0, mlv2[0]], [0, mlv2[1]], 'k', linewidth=1)
        plt.plot([mlv1[0], mlv1[0] + mlv2[0]], [mlv1[1], mlv1[1] + mlv2[1]], 'k', linewidth=1)
        plt.plot([mlv2[0], mlv1[0] + mlv2[0]], [mlv2[1], mlv1[1] + mlv2[1]], 'k', linewidth=1)

        # set equal aspect ratio
        plt.gca().set_aspect('equal', adjustable='box')
        # plt.grid()
        # plt.show()
        # plt.savefig("moire.pdf", bbox_inches='tight')

    def _validate_input1(self, a, name):
        if a is None:
            a = 0
            print(f"WARNING: {name} is not set, setting it to 0")
        if callable(a): return a
        return lambda this_coo, neigh_coo, this_type, neigh_type: a

    def _validate_input2(self, a, name):
        if a is None:
            a = 0
            print(f"WARNING: {name} is not set, setting it to 0")
        if callable(a): return a
        return lambda this_coo, this_type: a

    def generate_hamiltonian(
        self,
        tll: Union[float, int, Callable[[float], float]] = None,
        tuu: Union[float, int, Callable[[float], float]] = None,
        tlu: Union[float, int, Callable[[float], float]] = None,
        tul: Union[float, int, Callable[[float], float]] = None,
        tuself: Union[float, int, Callable[[float], float]] = None,
        tlself: Union[float, int, Callable[[float], float]] = None,
        data_type: np.dtype = np.float64,  # set to np.complex128 if you want complex numbers
    ):
        k = self.orbitals
        if tll is None or isinstance(tll, int) or isinstance(tll, float): tll = self._validate_input1(tll, "tll")
        if tuu is None or isinstance(tuu, int) or isinstance(tuu, float): tuu = self._validate_input1(tuu, "tuu")
        if tlu is None or isinstance(tlu, int) or isinstance(tlu, float): tlu = self._validate_input1(tlu, "tlu")
        if tul is None or isinstance(tul, int) or isinstance(tul, float): tul = self._validate_input1(tul, "tul")
        if tuself is None or isinstance(tuself, int) or isinstance(tuself, float): tuself = self._validate_input2(tuself, "tuself")
        if tlself is None or isinstance(tlself, int) or isinstance(tlself, float): tlself = self._validate_input2(tlself, "tlself")
        assert (
                callable(tll)
            and callable(tuu)
            and callable(tlu)
            and callable(tul)
            and callable(tuself)
            and callable(tlself)
        ), "tuu, tll, tlu, tul, tuself and tlself must be floats, ints or callable objects like functions"
        # self.plot_lattice()

        # 1. interaction inside the lower lattice
        ham_ll = np.zeros((len(self.lower_lattice.points)*k, len(self.lower_lattice.points)*k), dtype=data_type)
        _, indices = self.lower_lattice.first_nearest_neighbours(self.lower_lattice.points, self.lower_lattice.point_types)
        for i in range(len(self.lower_lattice.points)):  # self interactions
            ham_ll[i*k:(i+1)*k, i*k:(i+1)*k] += tlself(
                self.lower_lattice.points[i],
                self.lower_lattice.point_types[i]
            )
        for this_i in range(len(self.lower_lattice.points)):  # neighbour interactions
            this_coo = self.lower_lattice.points[this_i]
            this_type = self.lower_lattice.point_types[this_i]
            for neigh_i in indices[this_i]:
                neigh_coo = self.lower_lattice.points[neigh_i]
                neigh_type = self.lower_lattice.point_types[neigh_i]
                # ham_ll[this_i, neigh_i] += tuu(this_coo, neigh_coo, this_type, neigh_type)
                ham_ll[this_i*k:(this_i+1)*k, neigh_i*k:(neigh_i+1)*k] += tuu(this_coo, neigh_coo, this_type, neigh_type)

        # 2. interaction inside the upper lattice
        ham_uu = np.zeros((len(self.upper_lattice.points)*k, len(self.upper_lattice.points)*k), dtype=data_type)
        _, indices = self.upper_lattice.first_nearest_neighbours(self.upper_lattice.points, self.upper_lattice.point_types)
        for i in range(len(self.upper_lattice.points)):  # self interactions
            ham_uu[i*k:(i+1)*k, i*k:(i+1)*k] += tuself(
                self.upper_lattice.points[i],
                self.upper_lattice.point_types[i]
            )
        for this_i in range(len(self.upper_lattice.points)):  # neighbour interactions
            this_coo = self.upper_lattice.points[this_i]
            this_type = self.upper_lattice.point_types[this_i]
            for neigh_i in indices[this_i]:
                neigh_coo = self.upper_lattice.points[neigh_i]
                neigh_type = self.upper_lattice.point_types[neigh_i]
                ham_uu[this_i*k:(this_i+1)*k, neigh_i*k:(neigh_i+1)*k] += tll(this_coo, neigh_coo, this_type, neigh_type)

        # 3. interaction from the lower to the upper lattice
        ham_lu = np.zeros((len(self.lower_lattice.points)*k, len(self.upper_lattice.points)*k), dtype=data_type)
        _, indices = self.upper_lattice.query(self.lower_lattice.points, k=1)
        for this_i in range(len(self.lower_lattice.points)):
            neigh_i = indices[this_i, 0]
            ham_lu[this_i*k:(this_i+1)*k, neigh_i*k:(neigh_i+1)*k] += tlu(
                self.lower_lattice.points[this_i],
                self.upper_lattice.points[neigh_i],
                self.lower_lattice.point_types[this_i],
                self.upper_lattice.point_types[neigh_i],
            )

        # 4. interaction from the upper to the lower lattice
        ham_ul = np.zeros((len(self.upper_lattice.points)*k, len(self.lower_lattice.points)*k), dtype=data_type)
        _, indices = self.lower_lattice.query(self.upper_lattice.points, k=1)
        for this_i in range(len(self.upper_lattice.points)):
            neigh_i = indices[this_i, 0]
            ham_ul[this_i*k:(this_i+1)*k, neigh_i*k:(neigh_i+1)*k] += tul(
                self.upper_lattice.points[this_i],
                self.lower_lattice.points[neigh_i],
                self.upper_lattice.point_types[this_i],
                self.lower_lattice.point_types[neigh_i],
            )

        # # in ham_ll and ham_uu, check sum of all the rows...
        # # for constant t it should represent the number of neighbours for each point
        # print(f"unique sums in ham_ll: {np.unique(np.sum(ham_ll, axis=1))}")
        # print(f"unique sums in ham_uu: {np.unique(np.sum(ham_uu, axis=1))}")
        # print(f"unique sums in ham_lu: {np.unique(np.sum(ham_lu, axis=1))}")
        # print(f"unique sums in ham_ul: {np.unique(np.sum(ham_ul, axis=1))}")

        # combine the hamiltonians
        self.ham = np.block([
            [ham_ll, ham_lu],
            [ham_ul, ham_uu]
        ])

        return self.ham

    def generate_k_space_hamiltonian(
        self,
        k: np.ndarray,
        tll: Union[float, int, Callable[[float], float]] = None,
        tuu: Union[float, int, Callable[[float], float]] = None,
        tlu: Union[float, int, Callable[[float], float]] = None,
        tul: Union[float, int, Callable[[float], float]] = None,
        tuself: Union[float, int, Callable[[float], float]] = None,
        tlself: Union[float, int, Callable[[float], float]] = None,
        suppress_nxny_warning: bool = False,
    ):
        if suppress_nxny_warning is False and (self.nx != 1 or self.ny != 1):
            print("WARNING: atleast one of nx and ny are not 1, are you sure you want to use generate_k_space_hamiltonian with this lattice?")
        
        if tll is None or isinstance(tll, int) or isinstance(tll, float): tll = self._validate_input1(tll, "tll")
        if tuu is None or isinstance(tuu, int) or isinstance(tuu, float): tuu = self._validate_input1(tuu, "tuu")
        if tlu is None or isinstance(tlu, int) or isinstance(tlu, float): tlu = self._validate_input1(tlu, "tlu")
        if tul is None or isinstance(tul, int) or isinstance(tul, float): tul = self._validate_input1(tul, "tul")
        if tuself is None or isinstance(tuself, int) or isinstance(tuself, float): tuself = self._validate_input2(tuself, "tuself")
        if tlself is None or isinstance(tlself, int) or isinstance(tlself, float): tlself = self._validate_input2(tlself, "tlself")
        assert (
                callable(tll)
            and callable(tuu)
            and callable(tlu)
            and callable(tul)
            and callable(tuself)
            and callable(tlself)
        ), "tuu, tll, tlu, tul, tuself and tlself must be floats, ints or callable objects like functions"
        
        part = lambda k, this_coo, neigh_coo: np.exp(1j * (k @ (this_coo.squeeze() - neigh_coo.squeeze())))
        return self.generate_hamiltonian(
            lambda this_coo, neigh_coo, this_type, neigh_type: tll(this_coo, neigh_coo, this_type, neigh_type) * part(k, this_coo, neigh_coo),
            lambda this_coo, neigh_coo, this_type, neigh_type: tuu(this_coo, neigh_coo, this_type, neigh_type) * part(k, this_coo, neigh_coo),
            lambda this_coo, neigh_coo, this_type, neigh_type: tlu(this_coo, neigh_coo, this_type, neigh_type) * part(k, this_coo, neigh_coo),
            lambda this_coo, neigh_coo, this_type, neigh_type: tul(this_coo, neigh_coo, this_type, neigh_type) * part(k, this_coo, neigh_coo),
            tuself, tlself
        )





if __name__ == "__main__":
    from layers import SquareLayer, Rhombus60Layer, TriangularLayer, HexagonalLayer
    import time

    t = time.time()

    # lattice = MoireLattice(TriangularLayer, 9, 10, 3+0, 2+0, pbc=False)
    # lattice = MoireLattice(TriangularLayer, 3, 4, 20, 20, pbc=True, k=1)
    # lattice = MoireLattice(TriangularLayer, 3, 4, 4, 4, pbc=True, k=1)

    lattice = MoireLattice(HexagonalLayer, 9, 10, 2, 2, pbc=True, k=1)

    # lattice = MoireLattice(SquareLayer, 19, 20, 1, 1, pbc=True)
    # lattice = MoireLattice(TriangularLayer, 5, 6, 2, 2, pbc=True)
    # lattice = MoireLattice(TriangularLayer, 12, 13, 1, 1, pbc=True)
    # lattice = MoireLattice(TriangularLayer, 9, 10, 2, 4, pbc=False)


    # ham = lattice.generate_hamiltonian(1, 1, 1)

    # print(f"hamiltonian generation took: {time.time() - t:.2f} seconds")

    # # check if ham is hermitian
    # if np.allclose(ham, ham.T.conj()): print("Hamiltonian is hermitian.")
    # else: print("Hamiltonian is not hermitian.")

    # t = time.time()

    # evals, evecs = np.linalg.eigh(ham)

    # print(f"diagonalization took: {time.time() - t:.2f} seconds")


    # plt.imshow(ham, cmap="gray")
    # plt.colorbar()
    # plt.show()

    # lattice.plot_lattice()

    ham = lattice.generate_hamiltonian(1, 1, 1, 1, 1, 1)
    
    plt.imshow(ham, cmap="gray")
    plt.show()
