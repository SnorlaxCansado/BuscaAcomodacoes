// src/pages/AccommodationDetails.jsx
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getAcomodacaoById } from '../services/api';
import Spinner from '../components/Spinner';

const AccommodationDetails = () => {
  const { id } = useParams();
  const [accommodation, setAccommodation] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAccommodation = async () => {
      try {
        const response = await getAcomodacaoById(id);
        setAccommodation(response.data);
      } catch (error) {
        console.error('Erro ao buscar detalhes da acomodação:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchAccommodation();
  }, [id]);

  if (loading) return <Spinner />;
  if (!accommodation) return <p>Acomodação não encontrada.</p>;

  return (
    <div className="container mx-auto p-4">
      <img
        src={accommodation.imagem_url}
        alt={accommodation.nome}
        className="w-full h-64 object-cover rounded-md mb-4"
      />
      <h1 className="text-3xl font-bold mb-2">{accommodation.nome}</h1>
      <p className="text-xl text-gray-700 mb-2">{accommodation.cidade}</p>
      <p className="text-2xl font-semibold text-green-600 mb-4">
        R$ {accommodation.preco.toFixed(2)}
      </p>
    </div>
  );
};

export default AccommodationDetails;
