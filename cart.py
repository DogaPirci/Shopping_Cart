class ShoppingCart: 
    DISCOUNT_CODES = { 
        "SAVE10": {"type": "percent", "value": 10,  "min_order": 0.0}, 
        "SAVE20": {"type": "percent", "value": 20,  "min_order": 50.0}, 
        "FLAT5":  {"type": "fixed",   "value": 5.0, "min_order": 30.0}, 
    } 

    def __init__(self): 
        self._items = {} 
        self._discount = None 

    def add_item(self, name: str, price: float, quantity: int = 1) -> None: 
        if quantity <= 0: 
            raise ValueError("Quantity must be a positive integer.") 
        if price < 0: 
            raise ValueError("Price cannot be negative.") 
        if name in self._items: 
            self._items[name]["quantity"] += quantity
        else: 
            self._items[name] = {"price": price, "quantity": quantity} 

    def remove_item(self, name: str) -> None: 
        if name not in self._items: 
            raise KeyError(f"Item '{name}' is not in the cart.") 
        del self._items[name] 

    def apply_discount(self, code: str) -> None: 
        if code not in self.DISCOUNT_CODES: 
            raise ValueError(f"'{code}' is not a valid discount code.") 
        
        discount = self.DISCOUNT_CODES[code] 
        subtotal = self._subtotal() 
        
        if subtotal >= discount["min_order"]:
            self._discount = discount 
        else: 
            raise ValueError( 
                f"A minimum order of ${discount['min_order']:.2f} required. " 
                f"Your total: ${subtotal:.2f}." 
            ) 

    def get_total(self) -> float: 
        subtotal = self._subtotal() 
        if self._discount is None: 
            return round(subtotal, 2) 
        
        if self._discount["type"] == "percent": 
            amount = subtotal * (self._discount["value"] / 100.0)
            return round(max(0.0, subtotal - amount), 2) 
        
        return round(max(0.0, subtotal - self._discount["value"]), 2) 

    def clear(self) -> None: 
        self._items = {} 
        self._discount = None 

    def get_item_count(self) -> int:
        return sum(item["quantity"] for item in self._items.values()) 

    def _subtotal(self) -> float: 
        return sum( 
            item["price"] * item["quantity"] 
            for item in self._items.values() 
        )

# --- Test Örneği ---
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000.0, 1)
    cart.add_item("Mouse", 50.0, 2)
    cart.apply_discount("SAVE20")
    
    print(f"Toplam Ürün Sayısı: {cart.get_item_count()}")
    print(f"İndirimli Toplam Tutar: ${cart.get_total()}")