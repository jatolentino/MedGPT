<template>
    <section class="newsletter bg-accent md:h-[444px] py-12 flex items-center relative overflow-hidden">
      <div class="newsletter_container container mx-auto">
        <div class="flex flex-col lg:flex-row lg:items-center lg:gap-x-[58px]">
          <div class="flex-1 z-10 text-center lg:text-left">
            <div class="text-base uppercase text-white tracking-[2.24px] font-medium">Our newsletter</div>
            <h1 class="h1 mb-4 text-white">Subscribe to get more update</h1>
          </div>
          <form class="flex-1">
            <div class="flex flex-col md:flex-row relative gap-y-4">
              <input type="text" placeholder="Your email address" class="rounded-full w-full h-[66px] outline-none bg-transparent border-2 border-white pl-[30px] placeholder:text-white focus:text-white" />
              <button class="btn btn-lg btn-white md:absolute right-0">Subscribe</button>
            </div>
          </form>
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

            sr.reveal('.newsletter', { interval: 200 });
            sr.reveal('.newsletter_container', { interval: 200 });
            });
        }
    }
</script>
  
  <style scoped>
  /* Your scoped CSS here */
  </style>
  