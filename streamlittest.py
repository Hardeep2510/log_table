# import streamlit as st
# @st.cache
# def fetch(url):
#     return url
# def main():

#     d1 = fetch('https://www.google.com')
#     st.write("Result from fetching Google:", d1)

#     d2 = fetch('https://www.bing.com')
#     st.write("Result from fetching Bing:", d2)

#     d3 = fetch('https://www.google.com') 
#     st.write("Result from fetching Google (cached):", d3)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# @st.cache_data
# def give_output(argument):
#     st.write('hello')
#     return argument**2
# st.write(give_output(4))
# st.write(give_output(4))


# import streamlit as st
# import time
# # @st.cache_data
# # def my_function(x):
# #     time.sleep(5)
# #     return x * 2

 
# @st.cache_data
# def my_function(x):

#     time.sleep(5)



#     return x * 2
 
# st.write(my_function(5))
# st.write(my_function(5))


# import streamlit as st
# t1=(1,2,3)
# t2=(8,9)
# if not st.session_state:
#     st.session_state.fort1=t1
# t1=t1+t2
# st.write(st.session_state.fort1)



# import streamlit as st
# if (st.button("Button",key='button-key')):
#     st.write('You clicked')

# if(st.toggle('toggle',key='toggle-key')):
#     st.write('you toggled')

# if st.checkbox('Check me!', key='checkbox-key'):
#     st.write('You checked the box!')


# st.write(st.session_state)



import streamlit as st
def on_button_click(msg):
    st.write(msg)
    st.write(st.session_state.name)

st.session_state['name']='chris'

st.button("Button",key="my-button",on_click=on_button_click,args=("hi",))




