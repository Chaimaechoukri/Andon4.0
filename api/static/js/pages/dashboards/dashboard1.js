/*
Template Name: Admin Pro Admin
Author: Wrappixel
Email: niravjoshi87@gmail.com
File: js
*/
$(function () {
    "use strict";

    // ==============================================================
    // Sales overview
    // ==============================================================
    fetch('/api/capteur-data/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP! Statut: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Vérifier si les données sont valides
            if (!Array.isArray(data) || data.length === 0) {
                console.error('Aucune donnée disponible pour les capteurs.');
                return;
            }

            // Extraire les labels (refs) et les valeurs des capteurs
            const labels = data.map(item => item.ref);
            const values = data.map(item => item.value || 0); // Si pas de valeur, utiliser 0

            // Mettre à jour le graphique Chartist avec l'option barWidth
            new Chartist.Bar('.amp-pxl', {
                labels: labels,
                series: [values]
            }, {
                axisX: {
                    position: 'end',
                    showGrid: false
                },
                axisY: {
                    position: 'start'
                },
                high: Math.max(...values) + 10, // Ajuste la hauteur dynamique
                low: 0,
                barWidth: 100, // Changer la largeur des barres (ajuster la valeur ici)
                plugins: [
                    Chartist.plugins.tooltip()
                ]
            });
        })
        .catch(error => console.error('Erreur lors de la récupération des données :', error));

    // ==============================================================
    // Visitor overview
    // ==============================================================
    fetch('/api/visitor-data/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP! Statut: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Vérifier si les données sont valides
            if (!Array.isArray(data) || data.length === 0) {
                console.error('Aucune donnée disponible pour les visiteurs.');
                return;
            }

            // Préparer les données pour le graphique C3
            const columns = data.map(item => [item.ref, item.percentage]);

            // Mettre à jour le graphique C3 Donut
            var chart = c3.generate({
                bindto: '#visitor',
                data: {
                    columns: columns,
                    type: 'donut',
                    onclick: function (d, i) {
                        console.log("Capteur cliqué :", d.id, d.value);
                    },
                    onmouseover: function (d, i) {
                        console.log("Survol :", d.id, d.value);
                    },
                    onmouseout: function (d, i) {
                        console.log("Fin du survol :", d.id, d.value);
                    }
                },
                donut: {
                    label: {
                        show: true // Afficher les pourcentages dans le donut
                    },
                    title: "État En Panne (%)",
                    width: 30
                },
                legend: {
                    position: 'right' // Afficher la légende sur le côté droit
                },
                color: {
                    pattern: ['#ff4f4f', '#ffaf00', '#00c292', '#03a9f3'] // Couleurs personnalisées
                }
            });
        })
        .catch(error => console.error('Erreur lors de la récupération des données :', error));
});
