Using Jiwar in Google Colab
===========================

Google Colab provides a free, cloud-based environment for running Python code. This guide will help you use Jiwar in Google Colab using the provided Jiwar_Tutorial.ipynb notebook.

Getting Started with Jiwar in Google Colab
------------------------------------------

1. Open the Jiwar Tutorial Notebook:
   
   Click `HERE <https://colab.research.google.com/drive/1f_n7uuimT8MReaOW4U4LP8dAUVtY2hAq?usp=sharing>`_ to access the interactive Google Colab notebook for Jiwar.

2. Run the cells in the notebook sequentially, following the instructions provided.

Step 1: Clone Jiwar and Install Dependencies
-------------------------------------------

Run the following cells to set up Jiwar in your Colab environment:

1. Clone the Jiwar repository:

   .. code-block:: python

      !git clone https://github.com/AlaaAlzahrani/Jiwar.git

2. Install dependencies:

   .. code-block:: python

      %cd Jiwar
      !pip install --upgrade pip
      !pip install -r requirements.txt

3. Install eSpeak on Google Colab:

   .. code-block:: python

      !sudo apt-get update
      !sudo apt-get install -y espeak

Step 2: Run Jiwar
-----------------

The notebook provides two scenarios for running Jiwar: with a built-in corpus and with a custom corpus.

Using Jiwar with a Built-in Corpus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the cell containing:

.. code-block:: python

   !python jiwar.py

When prompted:

1. Enter the language (e.g., "en-us" for American English)
2. Choose to use the built-in corpus by entering "y"
3. Provide the input file path (e.g., "/content/Jiwar/data/input/en_words.csv")
4. Specify the measures to calculate (e.g., "all" for all measures)

Using Jiwar with a Custom Corpus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the same cell as above:

.. code-block:: python

   !python jiwar.py

When prompted:

1. Enter the language code
2. Choose not to use the built-in corpus by entering "n"
3. Provide the path to your custom corpus file (e.g., "/content/Jiwar/data/corpus/user_loaded/en_corpus.csv")
4. Provide the input file path
5. Specify the measures to calculate

Tips for Using Jiwar in Colab
-----------------------------

1. **Input Files**: Ensure your input files (word lists and custom corpora) are accessible in the Colab environment. You can upload them directly to Colab or store them in Google Drive and mount your drive.

2. **Output**: Jiwar will save the results as a CSV file. In Colab, you can download this file or save it to your Google Drive for further analysis.

Troubleshooting
---------------

If you encounter issues while using Jiwar in Google Colab:

1. Ensure all cells have run successfully, especially the setup and installation cells.
2. Check that your input files are in the correct location and format.
3. If you're using a custom corpus, make sure it meets the required format specifications.
4. Restart the runtime if you've made significant changes to the environment.
5. If problems persist, consult the Jiwar documentation or reach out to the author for support.
