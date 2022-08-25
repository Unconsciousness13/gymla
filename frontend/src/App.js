import "./App.css";
// import '../src/assets/css/slider.scss';
import React from "react";
import { Routes, Route } from "react-router-dom";
import Gallery from "./pages/Gallery";
import Videos from "./pages/Videos";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Slider from "./components/Slider";



// const slides = [
//   {
//     city: 'Habilitat',
//     img: 'https://i.ibb.co/ymTPPhH/1.jpg',
//   },
//   {
//     city: 'Singapore',
//     img: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/142996/singapore.jpg',
//   },
//   {
//     city: 'Prague',
//     img: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/142996/prague.jpg',
//   },
//   {
//     city: 'Amsterdam',
//     img: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/142996/amsterdam.jpg',
//   },
//   {
//     city: 'Moscow',
//     img: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/142996/moscow.jpg',
//   },
// ];


function App() {
  return (
    <div className="App">
      <Navbar />
        {/* <Slider slides={slides}/> */}
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
