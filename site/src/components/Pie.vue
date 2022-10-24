<script setup lang="ts">
import { Pie } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement,
} from "chart.js";
import { ref } from "vue";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement
);

let data = ref([93.2, 6.8]);
let data3 = ref([94.7, 5.3]);
let data2 = ref([91.7,1.4, 6.9]);
let label = ref(["Positive", "Negative"]);
let label2 = ref(["Positive", "Neutral", "Negative"]);
</script>
<template>
  <div class="grid grid-cols-3 gap-20">
    <div>
      <p>Distribution of Netflix reputation in the UK over the last decade</p>
      <Pie
        :chart-options="{
          maintainAspectRatio: false,
          responsive: true,
        }"
        :chart-data="{
          datasets: [
            {
              label: 'TEST',
              data: data,
              backgroundColor: ['#22C55E', '#E80000'],
            },
          ],
          labels: label,
        }"
      >
      </Pie>
    </div>
    <div>
      <p>Distribution of Netflix reputation in the US over the last decade</p>
      <Pie
        :chart-options="{
          maintainAspectRatio: false,
          responsive: true,
        }"
        :chart-data="{
          datasets: [
            {
              data: data2,
              backgroundColor: ['#22C55E','#22D3EE','#E80000'],
            },
          ],
          labels: label2,
        }"
      >
      </Pie>
    </div>
    <div>
      <p>Distribution of Netflix reputation in France over the last decade</p>
      <Pie
        :chart-options="{
          maintainAspectRatio: false,
          responsive: true,
        }"
        :chart-data="{
          datasets: [
            {
              label: 'TEST',
              data: data3,
              backgroundColor: ['#22C55E', '#E80000'],
            },
          ],
          labels: label,
        }"
      >
      </Pie>
    </div>
  </div>
</template>
