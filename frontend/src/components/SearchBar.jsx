// src/components/SearchBar.jsx
import React from 'react';
import { FiSearch } from 'react-icons/fi';

const SearchBar = ({ cidade, setCidade, isHero = false }) => {
  /*
    isHero: boolean que indica se a barra está sendo usada no Hero ou não.
    Isso permite ajustar algumas classes para visual levemente diferente
    (por ex. bordas mais espessas, cor do texto, etc.)
  */
  return (
    <div className="relative mb-4">
      <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">
        <FiSearch />
      </span>
      <input
        type="text"
        value={cidade}
        onChange={(e) => setCidade(e.target.value)}
        placeholder="Buscar por cidade..."
        className={`
          w-full pl-10 p-3 rounded-md 
          focus:outline-none focus:ring-2 focus:ring-blue-500
          ${isHero ? 'border-2 border-white text-gray-800 bg-white' : 'border border-gray-300 text-gray-800'}
        `}
      />
    </div>
  );
};

export default SearchBar;
