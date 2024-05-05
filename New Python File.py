# Import thư viện cần thiết
import streamlit as st

# Tạo tiêu đề cho ứng dụng
st.title('Ứng dụng Streamlit đơn giản')

# Tạo một input box cho người dùng nhập vào
user_input = st.text_input("Hãy nhập vào một câu", 'hello')

# Hiển thị câu vừa nhập
st.write(f'Bạn vừa nhập: {user_input}')
