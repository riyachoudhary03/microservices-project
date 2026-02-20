import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "15px", background: "black" }}>
      <Link to="/" style={{ color: "white", marginRight: "15px" }}>
        Home
      </Link>

      <Link to="/products" style={{ color: "white", marginRight: "15px" }}>
        Products
      </Link>

      <Link to="/orders" style={{ color: "white" }}>
        Orders
      </Link>
    </nav>
  );
}