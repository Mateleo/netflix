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

await axios.get("https://apidatacamp.4esport.fr/api/cw2").then((response) => {
  data.value = response.data.map((e:Array<string>) => e[0]);
  label.value = response.data.map((e:Array<number>) => e[1]);
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
          label: 'Words',
          data: label,
          backgroundColor:['#2563eb']
        },
      ],
      labels: data,
    }"
  >
  </Bar>
</template>
<style></style>
