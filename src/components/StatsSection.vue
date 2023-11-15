<template>
  <section class="stats section">
    <div class="container mx-auto">
      <!-- WRAPPER -->
      <div class="flex flex-col lg:flex-row gap-y-6 justify-between">
        <!-- ITEM -->
        <div class="stats_item flex-1 xl:border-r flex flex-col items-center lg:border-r-2">
          <div class="text-4xl xl:text-[64px] font-semibold 
          text-accent-tertiary xl:mb-2">+4500</div>
          <div>Happy Patients</div>
        </div>
        <!-- ITEM -->
        <div class="stats_item flex-1 xl:border-r flex flex-col items-center lg:border-r-2">
          <div class="text-4xl xl:text-[64px] font-semibold 
          text-accent-tertiary xl:mb-2">+10</div>
          <div>Specialties</div>
        </div>
        <!-- ITEM -->
        <div class="stats_item flex-1 xl:border-r flex flex-col items-center lg:border-r-2">
          <div class="text-4xl xl:text-[64px] font-semibold 
          text-accent-tertiary xl:mb-2">+10</div>
          <div>Years Experience</div>
        </div>
        <!-- ITEM -->
        <div class="stats_item flex-1 xl:border-r flex flex-col items-center">
          <div class="text-4xl xl:text-[64px] font-semibold 
          text-accent-tertiary xl:mb-2">+36</div>
          <div>Senior Doctors</div>
        </div>
      </div>
    </div>
  </section>
</template>
  
  <script>
  export default {
    mounted() {
      // Initialize ScrollReveal
      import('scrollreveal').then(ScrollReveal => {
        const sr = ScrollReveal.default({
          origin: 'bottom',
          distance: '30px',
          duration: 1000,
          delay: 100
        });
  
        sr.reveal('.stats_item', { interval: 200 })
      });
    }
  }
  </script>
  
  <style scoped>
  /* Your scoped CSS here */
  </style>
  sr.reveal('.stats_item', {interval: 200});