import streamlit as st
import pandas as pd

# Data for class descriptions
class_data = {
    'Class': ['Math', 'Science', 'History', 'Art'],
    'Description': [
        'Mathematics is the study of numbers, quantities, and shapes.',
        'Science is the systematic study of the structure and behavior of the physical, biological, and social world.',
        'History is the study of past events, particularly in human affairs.',
        'Art is the expression or application of human creative skill and imagination.'
    ]
}

class_df = pd.DataFrame(class_data)

# List to store student data
students = []

def main():
    st.title("Student Class Selection")

    with st.form(key='student_form'):
        name = st.text_input("Student Name:")
        classes = st.multiselect(
            "Select Classes:",
            class_df['Class'].tolist()
        )
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            student = {'name': name, 'classes': classes}
            students.append(student)
            st.success("Student added successfully!")

    st.header("Summary of Class Selections")

    if students:
        df = pd.DataFrame(students)
        df = df.explode('classes')
        df_with_desc = pd.merge(df, class_df, left_on='classes', right_on='Class', how='left')
        st.write(df_with_desc[['name', 'classes', 'Description']])

if __name__ == '__main__':
    main()
