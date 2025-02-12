// src/components/FavoriteButton.jsx
import React, { useState, useEffect } from 'react';

const FavoriteButton = ({ id }) => {
  const [isFavorite, setIsFavorite] = useState(false);

  // Verifica se o item já está nos favoritos ao montar ou quando o "id" mudar
  useEffect(() => {
    const favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    setIsFavorite(favoritos.includes(id));
  }, [id]);

  const toggleFavorite = (e) => {
    // Previne que o clique no botão acione a navegação do Link
    e.stopPropagation();
    const favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    let updatedFavorites;
    if (favoritos.includes(id)) {
      updatedFavorites = favoritos.filter((favId) => favId !== id);
    } else {
      updatedFavorites = [...favoritos, id];
    }
    localStorage.setItem('favoritos', JSON.stringify(updatedFavorites));
    setIsFavorite(!isFavorite);
  };

  return (
    <button
      onClick={toggleFavorite}
      className={`p-2 rounded-full ${isFavorite ? 'bg-red-500 text-white' : 'bg-gray-200 text-gray-800'}`}
      title={isFavorite ? 'Remover dos favoritos' : 'Adicionar aos favoritos'}
    >
      {isFavorite ? '♥' : '♡'}
    </button>
  );
};

export default FavoriteButton;
