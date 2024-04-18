import { Container, Navbar, Nav } from "react-bootstrap";
import Header from "./components/Header";
import Footer from "./components/Footer";
import "./bootstrap.min.css";

function App() {
  return (
    <>
      <Header />
      <main className="py-3">
        <Navbar
          data-bs-theme="dark"
          expand="lg"
          className="bg-body-tertiary"
          collapseOnSelect
        >
          <Container>
            <Navbar.Brand href="/">ProShop</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="ml-auto">
                <Nav.Link href="/cart">
                  <i className="fas fa-shopping-cart"></i>Cart
                </Nav.Link>
                <Nav.Link href="/login">
                  <i className="fas fa-user"></i>Login
                </Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
        <h1>Welcome</h1>
      </main>
      <Footer />
    </>
  );
}

export default App;
