// src/components/Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="w-full bg-blue-600 text-white py-4 px-4 flex justify-between items-center">
      <h1 className="text-xl sm:text-2xl font-bold">Locação de Temporada</h1>
      <div className="flex space-x-4">
        <Link to="/" className="hover:underline">Home</Link>
        <Link to="/favoritos" className="hover:underline">Favoritos</Link>
      </div>
    </nav>
  );
};

export default Navbar;
