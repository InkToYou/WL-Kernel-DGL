
import numpy as np
import networkx as nx
from wlkernel.weisfeiler_lehman import is_possibly_isomorphic


class TestIsIsormorphic:
  def test_path_graph(self):
    for i in range(10):
      N = np.random.randint(2, 50)
      G = nx.path_graph(N)
      mapping = {i: j for i, j in zip(
          range(N), np.random.permutation(range(N)))}
      H = nx.relabel_nodes(G, mapping)

      assert nx.is_isomorphic(G, H)
      assert is_possibly_isomorphic(G, H, N)

  def test_tree(self):
    for i in range(10):
      N = np.random.randint(2, 50)
      G = nx.random_tree(N)
      mapping = {i: j for i, j in zip(
          range(N), np.random.permutation(range(N)))}
      H = nx.relabel_nodes(G, mapping)

      assert nx.is_isomorphic(G, H)
      assert is_possibly_isomorphic(G, H, N)

  def test_barabasi_albert_graph(self):
    for i in range(10):
      N = np.random.randint(10, 50)
      G = nx.barabasi_albert_graph(N, 3)
      mapping = {i: j for i, j in zip(
          range(N), np.random.permutation(range(N)))}
      H = nx.relabel_nodes(G, mapping)

      assert nx.is_isomorphic(G, H)
      assert is_possibly_isomorphic(G, H, N)


class TestIsNotIsormorphic:
  def test_different_number_of_nodes(self):
    for i in range(10):
      N1 = np.random.randint(10, 50)
      N2 = np.random.randint(10, 50)
      if N1 == N2:
        N1 = N2 + np.random.randint(1, 10)
      G = nx.barabasi_albert_graph(N1, 3)
      H = nx.barabasi_albert_graph(N2, 3)

      assert not nx.is_isomorphic(G, H)
      assert not is_possibly_isomorphic(G, H, max(N1, N2))

  def test_different_number_of_edges(self):
    for i in range(10):
      N = np.random.randint(2, 50)
      E1 = np.random.randint(N * (N - 1) / 2 - 1)
      E2 = np.random.randint(N * (N - 1) / 2 - 1)
      if E1 == E2:
        E1 -= 1
      G = nx.gnm_random_graph(N, E1)
      H = nx.gnm_random_graph(N, E2)

      assert not nx.is_isomorphic(G, H)
      assert not is_possibly_isomorphic(G, H, N)
