<template>
    <section class="hero bg-grey py-12 xl:pt-12 xl:pb-0 overflow-hidden">
      <div class="container mx-auto gap-y-2 lg:flex lg:justify-around h-full">
        <div class="hero_text xl:w-[48%] flex flex-col text-center lg:justify-start lg:text-left xl:text-left">
          <div class="flex items-center bg-white py-[10px] px-[20px] w-max gap-x-2 mb-[26px] rounded-full mx-auto lg:mx-0 lg:mt-9">
            <i class="ri-heart-pulse-line text-2xl text-accent"></i>
            <div class="uppercase text-base font-medium text-[#9ab4b7] tracking-24px]">
              Live your life
            </div>
          </div>
          <h1 class="h2 mb-6">Healthcare for Every Step of Your Journey</h1>
          <p class="mb-[42px] md:max-w-xl">
            Exceptional Care, Advanced Treatments and <br />
            Compassionate Support—Your Health is Our Priority
          </p>
          <button class="btn btn-sm lg:w-[240px] btn-accent mx-auto xl:mx-0">
            CONTACT US
          </button>
        </div>
        <div class="hero_img hidden lg:flex xl:flex max-w-[814px] self-end">
          <img src="../assets/img/docs.png" height="400px" alt="elham" />
        </div>
      </div>
    </section>
</template>
  
<script>
    export default {
        mounted() {
            // Initialize Swiper if needed
        //   import('swiper').then(Swiper => {
        //     new Swiper('.swiper', {
        //       loop: true,
        //       pagination: {
        //         el: '.swiper-pagination',
        //         clickable: true
        //       }
        //     });
        //   });
        import('scrollreveal').then(ScrollReveal => {
                const sr = ScrollReveal.default({
                origin: 'bottom',
                distance: '30px',
                duration: 1000,
                delay: 100
                });

                sr.reveal('.hero_text', { interval: 200 });
                sr.reveal('.hero_img', { interval: 200 });
            });

        }
}
</script>

<style scoped>
/* Your scoped CSS here */
</style>
