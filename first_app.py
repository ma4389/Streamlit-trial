import streamlit as st

st.title('Hello World')
st.header("this a header markdown")
st.markdown("hi is the mark down")
st.subheader("this a subheader")
st.caption("this is the caption")
st.code('''if x == 5 :
        print('hello')''')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.image("https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width = 200 )