from google.adk.agents import Agent
def get_product_details(product_name: str):
    """Gathers basic details about a product."""
    details = {
        "smartphone": "A cutting-edge smartphone with advanced camera features and lightning-fast processing.",
        "usb charger": "A super fast and light usb charger",
        "shoes": "High-performance running shoes designed for comfort, support, and speed.",
        "headphones": "Wireless headphones with advanced noise cancellation technology for immersive audio.",
        "speaker": "A voice-controlled smart speaker that plays music, sets alarms, and controls smart home devices.",
    }
    return details.get(product_name, "Product details not found.")



def get_product_price(product_name: str):
    """Gathers price about a product."""
    details = {
        "smartphone": 500,
        "usb charger": 10,
        "shoes": 100,
        "headphones": 50,
        "speaker": 80,
    }
    return details.get(product_name, "Product price not found.")

root_agent = Agent(
    name="product_price_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent to answer questions about product details and price"
    ),
    instruction=(
        "I can answer your questions about product details and price"
    ),
    tools=[get_product_details, get_product_price],
)
