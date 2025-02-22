from setuptools import setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        

        install.run(self)

        import os
        import shutil
        import zipfile
        import site
        import gdown

        site_packages = site.getsitepackages()

        _libd = None

        for path in site_packages:
            potential_path = os.path.join(path, "GEDSpy")
            if os.path.exists(potential_path):
                _libd = potential_path
                break

        
        URL = 'https://drive.google.com/uc?id=1LQXI7zEXyvywjBz2TX1QBXN60Abia6WP'

            
        gdown.download(URL, os.path.join(_libd, 'data.zip'))
        shutil.rmtree(os.path.join(_libd, 'data'), ignore_errors=True)
        os.makedirs(os.path.join(_libd, 'data'), exist_ok=True)
        with zipfile.ZipFile(os.path.join(_libd, 'data.zip'), 'r') as zipf:
            zipf.extractall(os.path.join(_libd, 'data'))
        os.remove(os.path.join(_libd, 'data.zip'))
               
            


setup(
    name="GEDSpy", 
    version='2.1.5',
    author="Jakub Kubis - JBS",
    author_email="jbiosystem@gmail.com",
    description='GEDSpy (Gene Enrichment for Drug Searching)',
    long_description='GEDSpy is a Python library designed for the analysis of biological data, particularly in high-throughput omics studies. It is a powerful tool for RNA-seq, single-cell RNA-seq, proteomics, and other large-scale biological analyses where numerous differentially expressed genes or proteins are identified. GEDSpy leverages multiple renowned biological databases to enhance functional analysis, pathway enrichment, and interaction studies. It integrates data from: Gene Ontology (A structured framework for gene function classification) , Kyoto Encyclopedia of Genes and Genomes (A resource for understanding high-level functions and utilities of biological systems), Reactome (A curated knowledge base of biological pathways), Human Protein Atlas (A comprehensive database of human protein expression), NCBI (A vast repository of genetic and biomedical data), STRING (A database of known and predicted protein-protein interactions), IntAct (A repository of molecular interaction data), CellTalk (A database for intercellular communication analysis), CellPhone (A tool for inferring cell-cell interactions from single-cell transcriptomics), Human Diseases (A resource linking genes to diseases), ViMic (A database for microbial virulence factors). GEDSpy is designed to streamline biological data interpretation, enabling researchers to perform in-depth functional analyses, pathway enrichment, and drug target discovery. Its integration of multiple databases makes it an essential tool for translational research, biomarker identification, and disease mechanism exploration. Package description on https://github.com/jkubis96/GEDSpy',
    packages=['GEDSpy'],
    include_package_data=True,
    install_requires=[
        'requests', 
        'pandas', 
        'tqdm', 
        'seaborn', 
        'matplotlib', 
        'scipy', 
        'networkx', 
        'pyvis', 
        'beautifulsoup4', 
        'numpy', 
        'adjustText', 
        'gdown', 
        'pkg_resources', 
        'fisher-exact',  
        'binom-test',    
        'urllib3',       
        'bs4',           
    ],       
    keywords=['RNA_seq', 'SEQ', 'GO', 'pathways', 'interactions', 'gene ontology', 'diseases', 'enrichment', 'OMIC'],
    license='GPL-3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    cmdclass={
        "install": CustomInstallCommand,
    },
)
