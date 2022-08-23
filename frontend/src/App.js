import "./App.css";
import React from "react";
import { Routes, Route } from "react-router-dom";
import Gallery from "./pages/Gallery";
import Videos from "./pages/Videos";

import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Slider from "./components/Slider";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Slider />
      <Routes>
        <Route path="/videos" element={<Videos />} />
        <Route path="/gallery" element={<Gallery />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
