import axios from 'axios';
import { getCookie } from './utils/utils';

export const api = axios.create({
  baseURL: 'http://localhost:8000/',
  timeout: 5000,
  withCredentials: true,
  headers: {
    'X-CSRFToken': getCookie('csrftoken'),
  },
});

export const PREDICT_URL = '/predict';
