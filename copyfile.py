import shutil

thefiles=["/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0529_Change My Heart, O God_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0554_As the Deer_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0557_More Precious than Silver_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0572_I Will Celebrate (BALOCHE)_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0588_Sanctuary_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0963_You Alone_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0925_Sweet Mercies_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0721_Jesus Paid It All_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0607_What a Day That Will Be_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0849_How Great Are You, Lord_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0968_You Are My All in All_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0592_Refiner's Fire_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0697_Blessed Assurance, Jesus Is Mine_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0719_It Is Well with My Soul_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0720_Jesus Paid It All_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0935_The Power of Your Love_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0862_I Want to Be Where You Are_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0776_Beautiful Savior_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0974_Your Name (BROMLEY)_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0950_We Are the Body of Christ_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0799_Eagle's Wings_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0833_He Will Come and Save You_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0847_How Can I Keep from Singing_Piano.pdf",
"/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/0957_Who Is There like You_Piano.pdf"]

for f in thefiles:
    thedest='pdfs/'+ f.replace("/Users/mthompson/Library/Mobile Documents/com~apple~CloudDocs/Documents/BaptistHymnal2008/All_Scores_Piano/","")
    shutil.copyfile(f,thedest)