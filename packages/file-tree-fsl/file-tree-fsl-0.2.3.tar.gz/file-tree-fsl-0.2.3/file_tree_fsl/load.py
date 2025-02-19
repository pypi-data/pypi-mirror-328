import sys
if sys.version_info > (3, 10):
    from importlib import resources as importlib_resources
else:
    import importlib_resources
from file_tree.parse_tree import available_subtrees


def load():
    for entry in importlib_resources.files('file_tree_fsl').joinpath('trees').iterdir():
        with entry.open('rb') as f:
            available_subtrees[entry.name] = f.read().decode()

    # allows different capitalisation for backwards compatibility
    available_subtrees['BedpostX.tree'] = available_subtrees['bedpostx.tree']
    available_subtrees['ProbtrackX.tree'] = available_subtrees['probtrackx.tree']
    available_subtrees['Diffusion.tree'] = available_subtrees['diffusion.tree']
    available_subtrees['HCP_Surface.tree'] = available_subtrees['HCP_surface.tree']
