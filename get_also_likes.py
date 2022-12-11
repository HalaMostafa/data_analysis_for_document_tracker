
from graphviz import Digraph
import numpy as np
import tempfile
from tkinter import messagebox
class Also:
    #Getting visitors list of a document
    def visitors_doc(self,Data,doc_uuid):
        #self.df.loc[self.df['env_type']=='reader'].copy()
        filtered=Data.loc[(Data['env_type']=='reader')& (Data['env_doc_id']==doc_uuid)].copy()
        return filtered['visitor_uuid'].unique()
    
    #Getting document lists of a particular visitor 
    def also_read(self,Data,visitor):
        filtered=Data.loc[Data['visitor_uuid']==visitor].copy()
        return filtered['env_doc_id'].unique()    
    
    #Getting also likes list        
    def also_likes(self,Data,doc_sort,doc_id,user_id):
        
        if len(doc_id)==0:
            messagebox.showinfo("Warning","Enter the document id")
        elif len(user_id)==0:
            messagebox.showinfo("Warning","Enter the user id")
        else: 

            #Getting users who read the given document
            other_users=self.visitors_doc(Data,doc_id)
            doc_hits={}
            user_doc={}
            
            #Getting other documents read by the above obtained users
            for each in other_users:
                user_doc[each]=self.also_read(Data,each).tolist()
                
            #Creating graph
            g = Digraph('G', filename='hello.gv')       
            for each in user_doc:
                for i in user_doc[each]:
                    if i is np.nan:
                        i=i                
                    else:    
                        g.node(each[-4:],shape='square')
                        g.edge(each[-4:],i[-4:])
            g.node_attr.update(color='lightblue2', style='filled')
            g.node(user_id[-4:],style='filled',fillcolor='green',shape='square')
            g.node(doc_id[-4:],color='green',style='filled')
            g.edge(user_id[-4:], doc_id[-4:])
            g.render(directory='doctest-output', view=True).replace('\\', '/')
            g.view(tempfile.mktemp('hello.gv'))


    
        
    def also_likes_sorted(self,Data,doc_sort,doc_id,user_id):
        
        if len(doc_id)==0:
            messagebox.showinfo("Warning","Enter the document id")
        elif len(user_id)==0:
            messagebox.showinfo("Warning","Enter the user id")
        else: 
            try:   
                #Getting users who read the given document
                other_users=self.visitors_doc(Data,doc_id)
                doc_hits={}
                user_doc={}
                
                #Getting other documents read by the above obtained users
                for each in other_users:
                    user_doc[each]=self.also_read(Data,each).tolist() 
                    
                #Creating sorted list
                for each in user_doc:
                    for i in user_doc[each]:
                        if i is np.nan:
                            i=i                
                        else:    
                            doc_hits[i]=doc_sort[i]                
            
                #Obtaining documents from the also likes list in sorted order
                doc_hits=sorted(doc_hits.items(), key=lambda y: y[1],reverse=True)
                if doc_hits=={}:
                    messagebox.showinfo("Warning","Entered document ID does not exist")
                 
            except Exception:
                messagebox.showinfo("Error","Check the IDs you entered")                  
          