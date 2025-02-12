// src/services/api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const getAcomodacoes = (cidade) => {
  const url = cidade 
    ? `${API_BASE_URL}/acomodacoes?cidade=${cidade}` 
    : `${API_BASE_URL}/acomodacoes`;
  return axios.get(url);
};

export const getAcomodacaoById = (id) => {
  return axios.get(`${API_BASE_URL}/acomodacoes/${id}`);
};
