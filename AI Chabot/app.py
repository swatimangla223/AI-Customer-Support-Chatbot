import streamlit as st

st.set_page_config(page_title="AI Customer Support Chatbot", page_icon="??", layout="centered")

st.title("?? AI Customer Support Chatbot")
st.caption("A simple Streamlit-based support assistant for common customer questions.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I can help with refunds, shipping, orders, billing, and account issues. What would you like help with?"}
    ]


def get_support_reply(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["refund", "return", "exchange"]):
        return "You can request a refund or return from your order details page. If the item was delivered incorrectly, reply with your order number and a photo so I can help escalate it."

    if any(word in text for word in ["ship", "delivery", "tracking", "arrive"]):
        return "Shipping usually takes 2-5 business days for standard orders. You can check the latest status in your order tracking page or I can help you locate your tracking number."

    if any(word in text for word in ["order", "purchase", "invoice"]):
        return "I can help you review your order history, check payment status, or confirm whether your purchase was completed successfully."

    if any(word in text for word in ["cancel", "stop", "remove"]):
        return "If your order has not shipped yet, it may still be possible to cancel it. Send me your order number and I will guide you through the next step."

    if any(word in text for word in ["payment", "billing", "charge", "card"]):
        return "If you see an unexpected charge, please confirm the amount, date, and last four digits of the card so I can help investigate it."

    if any(word in text for word in ["account", "login", "password", "email"]):
        return "If you are having trouble signing in, try resetting your password first. If the issue continues, I can help you troubleshoot your account access."

    if any(word in text for word in ["hello", "hi", "thanks", "thank you"]):
        return "You are welcome! I am here to help with support questions about orders, billing, shipping, returns, and account access."

    return "I can help with common support topics like refunds, shipping, orders, billing, and account access. Please tell me what you need assistance with."


with st.sidebar:
    st.header("Quick help")
    st.write("Try asking:")
    for example in ["How do I request a refund?", "Where is my order?", "I need help with billing."]:
        st.info(example)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask the support bot...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_support_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
