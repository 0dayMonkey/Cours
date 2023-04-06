class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def height(node):
    """Retourne la hauteur de l'arbre binaire représenté par le noeud donné."""
    if node is None:
        return -1
    else:
        return 1 + max(height(node.left), height(node.right))

def count_leaves(node):
    """Retourne le nombre de feuilles de l'arbre binaire représenté par le noeud donné."""
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return count_leaves(node.left) + count_leaves(node.right)

def count_internal_nodes(node):
    """Retourne le nombre de noeuds internes de l'arbre binaire représenté par le noeud donné."""
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 0
    else:
        return 1 + count_internal_nodes(node.left) + count_internal_nodes(node.right)



def is_binary_search_tree(node):
    """Retourne True si l'arbre binaire représenté par le noeud donné est un ABR, False sinon."""
    # Cas de l'arbre vide ou du noeud terminal
    if node is None or (node.left is None and node.right is None):
        return True
    # Cas du noeud avec un sous-arbre gauche seulement
    elif node.right is None:
        return node.value > node.left.value and is_binary_search_tree(node.left)
    # Cas du noeud avec un sous-arbre droit seulement
    elif node.left is None:
        return node.value < node.right.value and is_binary_search_tree(node.right)
    # Cas du noeud avec des sous-arbres gauche et droit
    else:
        return (node.value > node.left.value) and (node.value < node.right.value) and is_binary_search_tree(node.left) and is_binary_search_tree(node.right)














      

# Création de l'arbre binaire
root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))

# Calcul de la hauteur de l'arbre
h = height(root)
print(f"Hauteur de l'arbre : {h}")

# Calcul du nombre de feuilles de l'arbre
n_leaves = count_leaves(root)
print(f"Nombre de feuilles de l'arbre : {n_leaves}")

# Calcul du nombre de noeuds internes de l'arbre
n_internal_nodes = count_internal_nodes(root)
print(f"Nombre de noeuds internes de l'arbre : {n_internal_nodes}")

# Vérification que l'arbre est un ABR
result = is_binary_search_tree(root)
print(f"L'arbre est un ABR : {result}")

root.left.value = 10
result = is_binary_search_tree(root)
print(f"L'arbre est un ABR : {result}")


def print_tree(node, level=0):
    """Affiche l'arbre binaire représenté par le noeud donné de manière graphique dans le terminal."""
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-' * 3 + str(node.value))
        print_tree(node.left, level + 1)
