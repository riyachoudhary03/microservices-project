export function getProducts() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = true; // change to false to test error

      if (success) {
        resolve([
          { id: 1, name: "Laptop", price: 50000 },
          { id: 2, name: "Mobile Phone", price: 20000 },
          { id: 3, name: "Headphones", price: 3000 },
        ]);
      } else {
        reject("Failed to fetch products");
      }
    }, 1000);
  });
}