import streamlit as st


# Run the Streamlit app
st.set_page_config(page_title="BBD", page_icon="♻️")

# Set the title of the webpage
st.image("BBd.png", caption="{ BBD(भू भूमि धरा) }", use_column_width=True)

st.title("Transforming Waste into Wonder: Recycle Today, Reimagine Tomorrow")

# Create sections on the webpage
st.header("Welcome to BBD:wave:!")
st.subheader("Learn about recycling and make a positive impact on the environment.")

# Add text and information about recycling
st.write("Recycling is important for reducing waste and conserving resources. It involves converting waste materials into reusable products.")
st.write("Explore our website to find information about different types of recycling, how to recycle properly, and tips for reducing waste.")

# Add an image related to recycling
st.image("recycling.png", caption="{ भू भूमि धरा }", use_column_width=True)

# Create buttons for different sections of the website
if st.button("Learn About Types of Recycling"):
    st.markdown("""
    # Learn About Types of Recycling
    
    Recycling is a process of collecting, processing, and reusing materials that would otherwise be discarded as waste. The goal of recycling is to reduce the consumption of new raw materials, energy usage, and pollution while conserving resources and minimizing the impact on the environment. Recycling plays a vital role in sustainable waste management and helps mitigate the negative effects of excessive waste production.
    
    Here's a comprehensive overview of recycling:
    
    **Benefits of Recycling:**
    - **Resource Conservation:** Recycling helps conserve natural resources such as minerals, metals, water, and timber by reusing materials from existing products rather than extracting new resources.
    - **Energy Savings:** The recycling process often requires less energy compared to producing new products from raw materials. This reduction in energy consumption helps lower greenhouse gas emissions and combat climate change.
    - **Waste Reduction:** Recycling reduces the amount of waste sent to landfills and incinerators, thereby extending the lifespan of these waste management facilities.
    - **Pollution Reduction:** By recycling materials, there's less need for extracting and processing new raw materials, which can lead to pollution from mining and manufacturing activities.
    - **Job Creation:** The recycling industry generates employment opportunities in collection, processing, sorting, and selling of recyclable materials.
    
    **Commonly Recycled Materials:**
    - **Paper:** Newspapers, magazines, cardboard, office paper, and packaging materials are commonly recycled to make new paper products.
    - **Plastic:** Plastic bottles, containers, bags, and packaging can be recycled into new plastic products.
    - **Glass:** Glass bottles and jars are melted down and reformed into new glass items.
    - **Metal:** Aluminum cans, steel cans, and other metal products can be melted and used to create new metal products.
    - **Textiles:** Clothing, fabrics, and textiles can be recycled into new clothing or repurposed as cleaning rags or other materials.
    - **Electronics:** Electronic waste (e-waste) can be dismantled and its components reused or properly disposed of to prevent environmental contamination.
    
    ...
    
    Recycling is an integral part of the broader effort to promote sustainable living and environmental stewardship. By participating in recycling programs and making conscious choices about consumption and waste disposal, individuals and communities can contribute to a healthier planet.
    """)
    
if st.button("Tips for Effective Recycling", key="button_label"):
    st.markdown("""
    **Tips for Effective Recycling**
        
    Recycling is an important practice for reducing waste and conserving resources. Here are some tips to help you recycle effectively:
        
    1. Know What's Recyclable: Familiarize yourself with the recycling guidelines in your area. Understand which materials can be recycled and which cannot.
        
    2. Clean and Dry: Rinse out containers before recycling them to avoid contamination. Dry items like paper and cardboard to prevent them from getting wet and becoming unusable.
        
    3. Separate Materials: Sort recyclables into different bins for paper, plastic, glass, and metal. Proper sorting improves the quality of recycled materials.
        
    4. Remove Labels and Caps: Remove labels, caps, and lids from containers before recycling. These can interfere with the recycling process.
        
    5. Avoid Tanglers: Keep items like plastic bags, cords, and hoses out of your recycling bin. These can tangle in sorting machines.
        
    6. Reduce Plastic Use: Minimize your use of single-use plastics. Opt for reusable bags, bottles, and containers whenever possible.
        
    7. Donate or Repurpose: Consider donating items that are still in good condition or finding creative ways to repurpose materials instead of discarding them.
        
    8. Educate Others: Spread awareness about proper recycling practices among your family, friends, and community to create a positive impact.
        
    Remember, effective recycling is a collective effort that benefits the environment and conserves resources for future generations.
    """)
    # You can link this button to another page or section of your Streamlit app

import streamlit as st

# Assuming you have set up Streamlit as your framework

if st.button("Tips for Effective Recycling", key="recycling_tips"):
    st.markdown("""
    **Tips for Effective Recycling**
        
    Recycling is an important practice for reducing waste and conserving resources. Here are some tips to help you recycle effectively:
        
    1. Know What's Recyclable: Familiarize yourself with the recycling guidelines in your area. Understand which materials can be recycled and which cannot.
        
    2. Clean and Dry: Rinse out containers before recycling them to avoid contamination. Dry items like paper and cardboard to prevent them from getting wet and becoming unusable.
        
    3. Separate Materials: Sort recyclables into different bins for paper, plastic, glass, and metal. Proper sorting improves the quality of recycled materials.
        
    4. Remove Labels and Caps: Remove labels, caps, and lids from containers before recycling. These can interfere with the recycling process.
        
    5. Avoid Tanglers: Keep items like plastic bags, cords, and hoses out of your recycling bin. These can tangle in sorting machines.
        
    6. Reduce Plastic Use: Minimize your use of single-use plastics. Opt for reusable bags, bottles, and containers whenever possible.
        
    7. Donate or Repurpose: Consider donating items that are still in good condition or finding creative ways to repurpose materials instead of discarding them.
        
    8. Educate Others: Spread awareness about proper recycling practices among your family, friends, and community to create a positive impact.
        
    Remember, effective recycling is a collective effort that benefits the environment and conserves resources for future generations.
    """)

    # You can link this button to another page or section of your Streamlit app

# Add a footer with contact information
st.title("Contact us at 6239132120")

st.header(":mailbox: Get in touch with BBD")

contact_form = """
<style>
    .contact-form {
        width: 80%;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    .contact-form input[type="text"],
    .contact-form input[type="email"],
    .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .contact-form button {
        background-color: #007BFF;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
<div class="contact-form">
    <form action="https://formsubmit.co/tanveersingh1359@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
</div>
"""

st.markdown(contact_form, unsafe_allow_html=True)
