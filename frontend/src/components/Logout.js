import React, { useEffect } from 'react';
import axiosInstance from '../Axios';
import { useHistory } from 'react-router-dom';

export default function SignUp() {
	const history = useHistory();

	useEffect(() => {
        // creating an axios instance
		const response = axiosInstance.post('user/logout/blacklist/', {
			refresh_token: localStorage.getItem('refresh_token'),
		});
		localStorage.removeItem('access_token');
		localStorage.removeItem('refresh_token');
		axiosInstance.defaults.headers['Authorization'] = null;
        // redirect the user
		history.push('/login');
	});
	return <div>Logout</div>;
}