import streamlit as st 
import pandas as pd
import numpy as np
import requests
import json
import webbrowser

df = pd.read_pickle('popular.pkl')

books = pd.read_pickle('books.pkl')
similarity_scores = pd.read_pickle('similarity.pkl')
pt = pd.read_pickle('pt.pkl')
final_books = pd.read_pickle("final.pkl")



def recommend_book(book_name):
    # fetch index
    index = np.where(pt.index==book_name)[0][0]
   
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data=[]
    for i in similar_items:
        item=[]
        temp_df = final_books[final_books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        
        data.append(item) 
    return data

def fetch_book_details(book_name):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(book_name)
    response=requests.get(url)
    obj=response.json()
    book_details=[]
    ids = [id['id'] for id in obj['items']]
    ids = ids[0]
    title = obj['items'][0]['volumeInfo']['title']
    author = obj['items'][0]['volumeInfo']['authors'][0]
    publish_date= obj['items'][0]['volumeInfo']['publishedDate'] 
    image = obj['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    preview_link = obj['items'][0]['volumeInfo']['previewLink']
    info =  obj['items'][0]['volumeInfo']['infoLink']
    book_details.append(ids)
    book_details.append(title)
    
    book_details.append(author)
  
    book_details.append(publish_date)
    book_details.append(preview_link)
    book_details.append(info)
    book_details.append(image)
    print(book_details)
    return book_details



menu = ['top20','recommender','about']

option = st.sidebar.selectbox("Select One: ",menu)

if option == 'top20':
    st.title("Top 20 Books")
    st.text("")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image(df['Image-URL-M'][0])
        st.markdown(f"[{df['Book-Title'][0]}]({fetch_book_details(df['Book-Title'][0])[5]})")
       
        st.markdown(f"<b>Author:<b>{df['Book-Author'][0]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][0]}")
        st.markdown(f"rating - {round(df['avg_ratings'][0],2)}")
    with col2:
        st.image(df['Image-URL-M'][3])
        st.markdown(f"[{df['Book-Title'][3]}]({fetch_book_details(df['Book-Title'][3])[5]})")

        st.markdown(f"<b>Author:<b>{df['Book-Author'][3]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][3]}")
        st.markdown(f"rating - {round(df['avg_ratings'][3],2)}")
    with col3:
        st.image(df['Image-URL-M'][5])
        st.markdown(f"[{df['Book-Title'][5]}]({fetch_book_details(df['Book-Title'][5])[5]})")
     
        st.markdown(f"<b>Author:<b>{df['Book-Author'][5]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][5]}")
        st.markdown(f"rating - {round(df['avg_ratings'][5],2)}")
    with col4:
        st.image(df['Image-URL-M'][9])
        st.markdown(f"[{df['Book-Title'][9]}]({fetch_book_details(df['Book-Title'][9])[5]})")

        st.markdown(f"<b>Author:<b>{df['Book-Author'][9]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][9]}")
        st.markdown(f"rating - {round(df['avg_ratings'][9],2)}")

    st.text("")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image(df['Image-URL-M'][13])
        st.markdown(f"[{df['Book-Title'][13]}]({fetch_book_details(df['Book-Title'][13])[5]})")
        st.markdown(df['Book-Title'][13][0:40])
        st.markdown(f"<b>Author:<b>{df['Book-Author'][13]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][13]}")
        st.markdown(f"rating - {round(df['avg_ratings'][13],2)}")
    with col2:
        st.image(df['Image-URL-M'][16])
        st.markdown(f"[{df['Book-Title'][16]}]({fetch_book_details(df['Book-Title'][16])[5]})")
    
        st.markdown(f"<b>Author:<b>{df['Book-Author'][16]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][16]}")
        st.markdown(f"rating - {round(df['avg_ratings'][16],2)}")
    with col3:
        st.image(df['Image-URL-M'][17])
        st.markdown(f"[{df['Book-Title'][17]}]({fetch_book_details(df['Book-Title'][17])[5]})")
        st.markdown(f"<b>Author:<b>{df['Book-Author'][17]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][17]}")
        st.markdown(f"rating - {round(df['avg_ratings'][17],2)}")
    with col4:
        st.image(df['Image-URL-M'][26])
        st.markdown(f"[{df['Book-Title'][26]}]({fetch_book_details(df['Book-Title'][26])[5]})")
        st.markdown(df['Book-Title'][26][0:40])
        st.markdown(f"<b>Author:<b>{df['Book-Author'][26]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][26]}")
        st.markdown(f"rating - {round(df['avg_ratings'][26],2)}")

    st.text("")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image(df['Image-URL-M'][28])
        st.markdown(f"[{df['Book-Title'][17]}]({fetch_book_details(df['Book-Title'][17])[5]})")
    
        st.markdown(f"<b>Author:<b>{df['Book-Author'][28]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][28]}")
        st.markdown(f"rating - {round(df['avg_ratings'][28],2)}")
    with col2:
        st.image(df['Image-URL-M'][39])
        st.markdown(f"[{df['Book-Title'][39]}]({fetch_book_details(df['Book-Title'][39])[5]})")
     
        st.markdown(f"<b>Author:<b>{df['Book-Author'][39]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][39]}")
        st.markdown(f"rating - {round(df['avg_ratings'][39],2)}")
    with col3:
        st.image(df['Image-URL-M'][47])
        st.markdown(f"[{df['Book-Title'][47]}]({fetch_book_details(df['Book-Title'][47])[5]})")
      
        st.markdown(f"<b>Author:<b>{df['Book-Author'][47]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][47]}")
        st.markdown(f"rating - {round(df['avg_ratings'][47],2)}")
    with col4:
        st.image(df['Image-URL-M'][53])
        st.markdown(f"[{df['Book-Title'][53]}]({fetch_book_details(df['Book-Title'][53])[5]})")

        st.markdown(f"<b>Author:<b>{df['Book-Author'][53]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][53]}")
        st.markdown(f"rating - {round(df['avg_ratings'][53],2)}")

    st.text("")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image(df['Image-URL-M'][55])
        st.markdown(f"[{df['Book-Title'][55]}]({fetch_book_details(df['Book-Title'][55])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][55]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][55]}")
        st.markdown(f"rating - {round(df['avg_ratings'][55],2)}")
    with col2:
        st.image(df['Image-URL-M'][62])
        st.markdown(f"[{df['Book-Title'][62]}]({fetch_book_details(df['Book-Title'][62])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][62]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][62]}")
        st.markdown(f"rating - {round(df['avg_ratings'][62],2)}")
    with col3:
        st.image(df['Image-URL-M'][63])
        st.markdown(f"[{df['Book-Title'][63]}]({fetch_book_details(df['Book-Title'][63])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][63]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][63]}")
        st.markdown(f"rating - {round(df['avg_ratings'][63],2)}")
    with col4:
        st.image(df['Image-URL-M'][72])
        st.markdown(f"[{df['Book-Title'][72]}]({fetch_book_details(df['Book-Title'][72])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][72]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][72]}")
        st.markdown(f"rating - {round(df['avg_ratings'][72],2)}")
    

    st.text("")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image(df['Image-URL-M'][73])
        st.markdown(f"[{df['Book-Title'][73]}]({fetch_book_details(df['Book-Title'][73])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][73]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][73]}")
        st.markdown(f"rating - {round(df['avg_ratings'][73],2)}")
    with col2:
        st.image(df['Image-URL-M'][78])
        st.markdown(f"[{df['Book-Title'][78]}]({fetch_book_details(df['Book-Title'][78])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][78]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][78]}")
        st.markdown(f"rating - {round(df['avg_ratings'][78],2)}")
    with col3:
        st.image(df['Image-URL-M'][84])
        st.markdown(f"[{df['Book-Title'][84]}]({fetch_book_details(df['Book-Title'][84])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][84]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][84]}")
        st.markdown(f"rating - {round(df['avg_ratings'][84],2)}")
    with col4:
        st.image(df['Image-URL-M'][85])
        st.markdown(f"[{df['Book-Title'][85]}]({fetch_book_details(df['Book-Title'][85])[5]})")
        
        st.markdown(f"<b>Author:<b>{df['Book-Author'][85]}",unsafe_allow_html=True)
        st.markdown(f"Votes - {df['num_ratings'][85]}")
        st.markdown(f"rating - {round(df['avg_ratings'][85],2)}")

elif option=='recommender':
    st.title("Books Recommender System")
    book_list = final_books['Book-Title'].values
    selected_book = st.selectbox("Select your book ",book_list)
    if st.button("show recommendation"):
        st.header("Recommend For You....")
        st.text("")
        data=recommend_book(selected_book)
        col1,col2,col3,col4=st.columns(4)
        
        with col1:
            st.image(fetch_book_details(data[0][0])[6])
            st.markdown(f"[{data[0][0]}]({fetch_book_details(data[0][0])[5]})")
           

        with col2:
            st.image(fetch_book_details(data[1][0])[6])
            st.markdown(f"[{data[1][0]}]({fetch_book_details(data[1][0])[5]})")
          
        with col3:
            st.image(fetch_book_details(data[2][0])[6])
            st.markdown(f"[{data[2][0]}]({fetch_book_details(data[2][0])[5]})")
        
      
        with col4:
            st.image(fetch_book_details(data[3][0])[6])
            st.markdown(f"[{data[3][0]}]({fetch_book_details(data[3][0])[5]})")
          

elif option=="about":
	st.title("Book Recommendation Engine V-2.0")
	st.markdown("This Engine Developed by <a href='https://github.com/datamind321'>DataMind Platform</a>",unsafe_allow_html=True)
	st.subheader("if you have any query Contact us on : bme19rahul.r@invertisuniversity.ac.in") 
	st.markdown("More on : ")
	
	
	st.markdown("[![Linkedin](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/rahul-rathour-402408231/)",unsafe_allow_html=True)
	

	st.markdown("[![Instagram](https://img.icons8.com/color/1x/instagram-new.png)](https://instagram.com/_technical__mind?igshid=YmMyMTA2M2Y=)")
      
    
