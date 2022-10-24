
------------------------------------------------------------------------------------------------------------------
                      
                                                                                                                                                                                                                  ༼ つ ◕_◕ ༽つ   README

------------------------------------------------------------------------------------------------------------------

                                             🥰 WELCOME DEAR TO "ER" 🥰
                                              
                                             Your E-Reputation with us !

------------------------------------------------------------------------------------------------------------------

--------------------------< To access our Dashboard web app page "ER" via web browser >----------------------------

------------------------------------------------------------------------------------------------------------------ 

  [1]- Click on "https://netflix-reputation.netlify.app/":
       ---> the web page will open on that browser!
       ---> Explore the informatiosn displayed there (•_•) !
     
------------------------------------------------------------------------------------------------------------------

----------------------<For the code of our solution to run you need to install the following >--------------------

------------------------------------------------------------------------------------------------------------------
📋 Requirments 

[1]. Install ANACONDA 
   Download it from : https://www.anaconda.com/

[2]. Open ANACONDA PowerShell prompt (installation of modules we'll be done here !)and type the commands 

[3]. Create a new environment: "You'll proceed to the creation of your own environment"  

--> Type:
    conda create -n my-env
    conda activate my-env

[4]. Add your Conda environment to your jupyter notebook (this step is VERY important because the python 3(ipykernel) 
     is linked to the base environement of ANACONDA)
     
This task is a 4 step. I'll walk you through it :

   *Step 1: install tensorflow  
   --> Type: conda install -c conda-forge tensorflow
   
   *Step 2: install ipykernel
   --> Type: conda install -c anaconda ipykernel
   
   *Step 3: Now comes the step to set this conda environment on your jupyter notebook, to do so please install ipykernel
   --> Type: python -m ipykernel install --user --name=my-env

[5]. Install numpy 
           
[6]. Install pandas 
           
[7]. Install Matplotlib 

[8]. Install seaborn 

[9]. Install scikit-learn 
      
[10]. Install NLTK 
   
[11]. Install wordcloud 
   
[12]. Install TextBlob     

[13]. Install vader Sentiment

[14]. Install GoogleNews

🛠 Installation

Copy and paste the following lines to ANACONDA powershell prompt:

conda config --env --add channels conda-forge
  
conda install numpy
  
conda install -c anaconda pandas
  
Conda install matplotlib
  
conda install -c anaconda seaborn
  
conda install -c anaconda nltk
  
conda install -c conda-forge nltk_data
  
conda install -c conda-forge wordcloud
  
conda install -c conda-forge textblob
  
python -m textblob.download_corpora
  
conda install -c conda-forge vadersentiment
  
pip install GoogleNews
------------------------------------------------------------------------------------------------------------------

------------------------ 🎊After all the installation is DONE, now the fun BEGINS 🎊------------------------------ 

------------------------------------------------------------------------------------------------------------------ 


------------------------------------------------------------------------------------------------------------------

-------------------------------------------< Solution Usage >-----------------------------------------------------

------------------------------------------------------------------------------------------------------------------ 
📊 Sentiment-Analysis

 [1]- From ANACONDA, OPEN JUPYTER NOTEBOOK(anaconda 3) 
       keep it open until the end of your journey on the web page

 [2]- DATA SOURCING
 
    [A]- If you would like to collect new Reviews about NETFLIX from Twitter, Open "Tweets_scraper.ipynb" 
         and execute it all via the icon ">>"

          ---> It will take you between 30 to 58 min to scrape 60000 tweets. So please be Patient!!!
          ---> Wait until all the notebook is executed 
          ---> Your dataset will be stored as a CSV File "tweets_dataset2.csv" as shown by the last entry In[15]. 
               You can change the name of the file as you like.
      
    [B]- * If you don't want to wait until the dataset is fully scraped, you can use the prepared dataset "TEST.csv" 
         in the dataset folder.
         * If you already have a dataset you would like to analyze, upload it in the folder Named 'dataset'.
           
 [3]- START THE SENTIMENT ANALYSIS
      Open "TEST.ipynb", change the the CSV file's name and execute the entire notebook using the icon ">>"

                       
     📛📛📛 WARNING: For the solution to work, you need to work in the created environment (my-env)📛📛📛
  The jupyter notebooks should be read under this environment (my-env) and not in the 'python 3(ipykernel)'!
 📛 thus, Make sure to change the "kernel" from 'python 3(ipykernel)'to 'my-env' for each of these notebooks 📛

📊 Netflix News Scraping

  [1]- Run Netflix_news_scraper.py in python
  [2]- The latest 10 news about Netflix in google news will be saved in the file "news_Netflix.csv"

     📛📛📛 WARNING: For this news scraper to work, you need to run it in software that executes python codes 📛📛📛
                        📛(like Python, Spyder,etc. ). It won't work on Jupyter Notebook📛 
 
📊 Deployed Solution 

   [1]- You can have a look at the magic behind our solution in this link: https://github.com/Mateleo/netflix.git 

------------------------------------------------------------------------------------------------------------------ 


 
--------------------------------------------- 🥰Have FUN DEAR 🥰------------------------------------------------
