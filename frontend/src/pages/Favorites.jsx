// src/pages/Favorites.jsx
import React, { useState, useEffect } from 'react';
import { getAcomodacaoById } from '../services/api';
import AccommodationCard from '../components/AccommodationCard';
import Spinner from '../components/Spinner';

const Favorites = () => {
  const [favoriteIds, setFavoriteIds] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);

  // Carrega os IDs dos favoritos armazenados no localStorage
  useEffect(() => {
    const favs = JSON.parse(localStorage.getItem('favoritos')) || [];
    setFavoriteIds(favs);
  }, []);

  useEffect(() => {
    const fetchFavorites = async () => {
      setLoading(true);
      try {
        const promises = favoriteIds.map((id) => getAcomodacaoById(id));
        const responses = await Promise.all(promises);
        const accommodationsData = responses.map((res) => res.data);
        setFavorites(accommodationsData);
      } catch (error) {
        console.error('Erro ao buscar acomodações favoritas:', error);
      } finally {
        setLoading(false);
      }
    };

    if (favoriteIds.length > 0) {
      fetchFavorites();
    } else {
      setFavorites([]);
      setLoading(false);
    }
  }, [favoriteIds]);

  return (
    <div className="container mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold mb-4">Meus Favoritos</h2>
      {loading ? (
        <Spinner />
      ) : favorites.length === 0 ? (
        <p className="text-gray-700">Você não possui acomodações favoritas.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {favorites.map((item) => (
            <AccommodationCard key={item.id} acomodacao={item} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Favorites;
