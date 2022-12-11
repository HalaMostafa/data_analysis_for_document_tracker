import tkinter as tk
from tkinter import ttk
from data_processing import dataProcessing
from charts import *
from analysis import documentTrackerAnalysis
from get_also_likes import Also

def renderTK(allAnalysis , window,Data,sort,docId,userId):
    objAlso=Also()

    btn_country=tk.Button(window,text="Views By Country",command=lambda:allAnalysis.getViewsByCountryContinents(countcolumn="country"))
    btn_country.grid(row=8,column=1,columnspan=2)

    btn_cont=tk.Button(window,text="Views By Continent",command=lambda:allAnalysis.getViewsByCountryContinents(countcolumn="continent"))
    btn_cont.grid(row=9,column=1,columnspan=2)

    btn_full_browser=tk.Button(window,text="Get Full Browser List",command=lambda:allAnalysis.get_full_browser())
    btn_full_browser.grid(row=10,column=1,columnspan=2)

    btn_browser=tk.Button(window,text="Get Browser List",command=lambda:allAnalysis.get_browser())
    btn_browser.grid(row=11,column=1,columnspan=2)

    btn_browser=tk.Button(window,text="Get Browser By OS",command=lambda:allAnalysis.getOSPerBrowser())
    btn_browser.grid(row=12,column=1,columnspan=2)

    btn_top_ten = tk.Button(window,text="Get Top Ten Users",command=lambda:allAnalysis.getTopTenUsers())
    btn_top_ten.grid(row=13,column=1,columnspan=2)

    btn_also=tk.Button(window,text="Get Also Likes",command=lambda:objAlso.also_likes(Data,sort,docId,userId))
    btn_also.grid(row=14,column=1,columnspan=2)


def gui():
    LARGE_FONT=('Verdana',12)
    # data that will be used in analysis
    allAnalysis = None
    #Creating GUI and adding controls    
    window=tk.Tk()
    window.title("Data Analysis For Document Tracker")
    def triggerButton(window):
        global allAnalysis
        dataObj=dataProcessing()#initialize data processing
        dataObj.getData()
        df = dataObj.df
        allAnalysis = documentTrackerAnalysis(userId=txt_userid.get(),documentId=txt_docid.get(),df=df) #initialize analysis class
        renderTK(allAnalysis, window,Data=df,sort = dataObj.get_sorted(),docId=txt_docid.get(),userId=txt_userid.get())

        

    photo = tk.PhotoImage(file = "icon.png")
    window.iconphoto(False, photo)

    #main label :
    label=tk.Label(window,text="Data Analysis",font=LARGE_FONT)
    label.grid(row=1,columnspan=4)

    # create browse label
    browse_label = tk.Label(window, text="Click Button to browse the Files")
    browse_label.grid(row=2)
    #create browse button
    browse_button = ttk.Button(window, text="Browse Data", command=lambda:triggerButton(window))
    browse_button.grid(row=2,column=2)


    label_docid=tk.Label(window,text="Document Id")
    label_userid=tk.Label(window,text="User Id")


    txt_docid=tk.Entry(window)
    txt_userid=tk.Entry(window)

    label_docid.grid(row=5)
    label_userid.grid(row=6)

    txt_docid.grid(row=5,column=2)
    txt_userid.grid(row=6,column=2)
    #get all Analysis
#c08fc48b49f0e1be
# 140206010823-b14c9d966be950314215c17923a04af7       
#------------
# 140224195414-e5a9acedd5eb6631bb6b39422fba6798
# 04daa9ed9dde73d3

    window.geometry("400x500+100+100")
    window.mainloop()

if __name__=='__main__':
    gui()