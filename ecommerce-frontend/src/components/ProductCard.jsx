export default function ProductCard({ product }) {
  return (
    <div
      style={{
        border: "1px solid gray",
        padding: "15px",
        marginBottom: "10px",
        borderRadius: "8px",
      }}
    >
      <h3>{product.name}</h3>
      <p>Price: ₹{product.price}</p>
    </div>
  );
}