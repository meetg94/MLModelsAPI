import { useState } from "react";

import fieldsConfig from '../fieldConfig.json';
import { api, PREDICT_URL } from '../api';
import { getCookie } from '../utils/utils.js';

function UserForm() {

    const initialFormState = fieldsConfig.reduce((acc, field) => ({ ...acc, [field.name]: '' }), {});
    const [formData, setFormData] = useState(initialFormState);

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        api.defaults.headers.post['X-CSRFToken'] = getCookie('csrftoken');
        api.post(PREDICT_URL, formData)
            .then(response => console.log(response))
            .catch(error => console.log(error));
    }

    const randomizeData = () => {
        let randomData = {}

        fieldsConfig.forEach((field) => {
            if (field.options) {
                let optionKeys = Object.keys(field.options);
                randomData[field.name] = optionKeys[Math.floor(Math.random() * optionKeys.length)];
            } else {
                randomData[field.name] = Math.floor(Math.random() * (field.max - field.min + 1) + field.min);
            }
        });
    
        setFormData(randomData);
    }

    return (
        <div>
            <form onSubmit={handleSubmit} className="">
                <h2>Genetic Information</h2>
                <div>
                {fieldsConfig.map((field, index) => {
                    if(field.options) {
                        return (
                            <div key={index} className="form-inputs">
                                <label>{field.label}</label>
                                <select 
                                    name={field.name} 
                                    value={formData[field.name]} 
                                    onChange={handleChange}
                                    required>
                                        <option value="">Select {field.label}</option>
                                        {Object.entries(field.options).map(([key, value]) => <option key={key} value={key}>{value}</option>)}
                                </select>
                            </div>
                        );
                    } else {
                        return (
                            <div key={index} className="form-inputs">
                                <label>{field.label}</label>
                                <input 
                                    type="number" 
                                    min={field.min} 
                                    max={field.max} 
                                    name={field.name}
                                    value={formData[field.name]}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                        )
                    }
                })}
                </div>
                <div className="form-button-container">
                    <button type="submit" className="form-button">Predict</button>
                    <button type="button" className="form-button" onClick={randomizeData}>Random Data</button>
                </div>
            </form>
        </div>
    );
};

export default UserForm
