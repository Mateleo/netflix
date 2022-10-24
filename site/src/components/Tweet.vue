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
let color = ref();

await axios.get("https://apidatacamp.4esport.fr/api/tw1").then((response) => {
  data.value = response.data.map((e: Array<number>) => e[0]);
  label.value = response.data.map((e: Array<number>) => e[1]);
  color.value = response.data.map((e: Array<string>) => e[2]);
  console.log(data.value);
});
</script>
<template>
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
          label: 'Polarity',
          data: label,
          backgroundColor: color,
        },
      ],
      labels: data,
    }"
  >
  </Bar>
</template>
<style></style>
