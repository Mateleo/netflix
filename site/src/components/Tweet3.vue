<script setup lang="ts">
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import { ref } from "vue";
import axios from "axios";

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

let data = ref();
let label = ref();

await axios.get("https://apidatacamp.4esport.fr/api/tw3").then((response) => {
  data.value = response.data.map((e: Array<number>) => e[0]);
  label.value = response.data.map((e: Array<number>) => e[1]);
  console.log(data.value);
});
</script>
<template>
  <h3 class="font-semibold text-xl mb-2 mt-20">Netflix tweets from the last decade</h3>
  <Bar
    :chart-options="{
      maintainAspectRatio: false,
      responsive: true,
      scales: {
        x: {
          ticks: {
            autoSkip: false,
          },
        },
      },
    }"
    :chart-data="{
      datasets: [
        {
          label: 'Tweets',
          data: label,
          backgroundColor: ['#2563eb'],
        },
      ],
      labels: data,
    }"
  >
  </Bar>
</template>
<style></style>
