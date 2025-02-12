// src/components/Hero.jsx
import React from 'react';
import SearchBar from './SearchBar';

const Hero = ({ cidade, setCidade }) => {
  return (
    <section className="w-full bg-blue-600 text-white py-8 px-4 flex flex-col items-center">
      <div className="w-full text-center">
        <h1 className="text-3xl md:text-4xl font-bold mb-3">
          Encontre o local perfeito para sua próxima viagem
        </h1>
        <p className="text-lg mb-5">
          Pesquise entre diversas acomodações disponíveis para locação de temporada
        </p>
        <div className="w-full px-4">
          <SearchBar cidade={cidade} setCidade={setCidade} isHero />
        </div>
      </div>
    </section>
  );
};

export default Hero;
