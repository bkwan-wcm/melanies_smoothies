# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
#  """Replace this example with your own code!
#  **And if you're new to Streamlit,** check
#  out our easy-to-follow guides at
#  [docs.streamlit.io](https://docs.streamlit.io).
#  """
)



# import streamlit as st
#option = st.selectbox(    
#    'What is your favorite fruit?',
#    ('Banana','Strawberries','Peaches'))

#st.write('Your favorite fruit is:',option)



Name_on_Order=st.text_input('Name on Smoothie:')
st.write('The name on your smoothis will be:',Name_on_Order)


cnx=st.connection("snowflake")
session=cnx.session()
#session = get_active_session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list=st.multiselect(
    'choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)

if ingredients_list:   #actually means if ingredients_list is not null#
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string=''

    for fruit_chosen in ingredients_list:
        ingredients_string+=fruit_chosen + ' '     #+= means add this to what is already in the variable #
                       #Ingredients_list and Ingredient_string are different varibles, dont mix them up #
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
        sf_dt=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)


    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,Name_on_Order)
            values ('""" + ingredients_string + """','""" +Name_on_Order+ """')"""

    st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert=st.button('Submit Order')

  
    #if ingredients_string:
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")


import requests



        
        
        
        



