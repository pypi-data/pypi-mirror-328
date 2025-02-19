import setuptools
import glob
import os.path as op

trees = glob.glob("trees/*.tree")
tree_dict = {
    f'{op.basename(tree)[:-5]}={tree}'
    for tree in glob.glob("trees/*.tree")
}


setuptools.setup(
    name="file-tree-fsl",
    version="0.2.3",
    url="https://git.fmrib.ox.ac.uk/fsl/file-tree-fsl",

    author="Michiel Cottaar",
    author_email="MichielCottaar@protonmail.com",

    description="Filetree definitions for the FSL neuroimaging library",
    long_description=open('README.md').read(),

    packages=('file_tree_fsl', ),

    package_data={'file_tree_fsl': ['trees/*.tree']},

    zip_safe=False,

    install_requires=[
        "file-tree",
        'importlib_resources; python_version < "3.10"',
    ],

    entry_points={'file_tree.trees': ['fsl=file_tree_fsl.load:load']},

    project_urls = {
        "Documentation": "https://open.win.ox.ac.uk/pages/fsl/file-tree/",
    },

    include_package_data=True,

    license="MIT",

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
    ],
)
