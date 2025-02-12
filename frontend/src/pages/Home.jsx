// src/pages/Home.jsx
import React, { useEffect, useState } from 'react';
import { getAcomodacoes } from '../services/api';
import Hero from '../components/Hero';
import AccommodationCard from '../components/AccommodationCard';
import Spinner from '../components/Spinner';

const Home = () => {
  const [acomodacoes, setAcomodacoes] = useState([]);
  const [cidade, setCidade] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchAcomodacoes = async () => {
    setLoading(true);
    try {
      const response = await getAcomodacoes(cidade);
      setAcomodacoes(response.data);
    } catch (error) {
      console.error('Erro ao buscar acomodações:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAcomodacoes();
  }, [cidade]);

  return (
    <div className="w-full">
      <Hero cidade={cidade} setCidade={setCidade} />
      <section className="w-full px-4 py-8">
        <h2 className="text-3xl font-bold mb-4">Acomodações Disponíveis</h2>
        {loading ? (
          <Spinner />
        ) : acomodacoes.length === 0 ? (
          <p className="text-gray-700">Nenhuma acomodação encontrada.</p>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {acomodacoes.map((item) => (
              <AccommodationCard key={item.id} acomodacao={item} />
            ))}
          </div>
        )}
      </section>
    </div>
  );
};

export default Home;
