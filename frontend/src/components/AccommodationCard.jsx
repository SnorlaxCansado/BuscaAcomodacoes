// src/components/AccommodationCard.jsx
import React from 'react';
import FavoriteButton from './FavoriteButton';
import { Link } from 'react-router-dom';

const AccommodationCard = ({ acomodacao }) => {
  const { id, nome, cidade, preco, imagem_url } = acomodacao;

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-xl">
      <Link to={`/acomodacao/${id}`}>
        <img
          src={imagem_url}
          alt={nome}
          className="w-full h-48 object-cover"
        />
      </Link>
      <div className="p-4">
        <Link to={`/acomodacao/${id}`}>
          <h2 className="text-xl font-semibold mb-2">{nome}</h2>
          <p className="text-gray-600 mb-1">{cidade}</p>
          <p className="text-green-600 font-bold mb-2">
            R$ {typeof preco === 'number' ? preco.toFixed(2) : '---'}
          </p>
        </Link>
        <div className="flex justify-end">
          <FavoriteButton id={id} />
        </div>
      </div>
    </div>
  );
};

export default AccommodationCard;
