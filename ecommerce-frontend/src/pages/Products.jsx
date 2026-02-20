import apiClient from "../api/apiClient";
import { useEffect, useState } from "react";
import { fetchProducts } from "../services/productService";
import ProductCard from "../components/ProductCard";

export default function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
  fetchProducts()
    .then((data) => {
      setProducts(data);
      setLoading(false);
    })
    .catch(() => {
      setError("Failed to fetch products");
      setLoading(false);
    });
}, []);

  // Loading UI
  if (loading) {
    return <h3>Loading products...</h3>;
  }

  // Error UI
  if (error) {
    return <h3 style={{ color: "red" }}>❌ {error}</h3>;
  }

  // Success UI
  return (
    <div>
      <h2>Products</h2>

      {products.map((item) => (
        <ProductCard key={item.id} product={item} />
      ))}
    </div>
  );
}