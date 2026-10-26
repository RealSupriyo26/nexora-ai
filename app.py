import streamlit as st

st.set_page_config(page_title="Nexora AI", page_icon="🤖", layout="centered")

st.title("🤖 Nexora AI Assistant")
st.write("আপনার নিজের প্রিমিয়াম এআই চ্যাট অ্যাপ্লিকেশন!")

# চ্যাট হিস্ট্রি সেভ রাখার জন্য
if "messages" not in st.session_state:
    st.session_state.messages = []

# আগের চ্যাটগুলো স্ক্রিনে দেখানোর জন্য
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট নেওয়ার বক্স
if prompt := st.chat_input("আপনার কি জানার আছে বলুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # এআই রেসপন্স
    with st.chat_message("assistant"):
        response = f"আপনি বলেছেন: {prompt}। খুব শীঘ্রই এখানে শক্তিশালী এআই এপিআই যুক্ত করা হবে!"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
      
