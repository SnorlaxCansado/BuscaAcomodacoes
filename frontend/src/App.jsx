// src/App.jsx
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Favorites from './pages/Favorites';
import AccommodationDetails from './pages/AccommodationDetails';
import Layout from './components/Layout';
import Navbar from './components/Navbar';
import './App.css';

function App() {
  return (
    <>
      <Navbar />
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/favoritos" element={<Favorites />} />
          <Route path="/acomodacao/:id" element={<AccommodationDetails />} />
        </Routes>
      </Layout>
    </>
  );
}

export default App;
