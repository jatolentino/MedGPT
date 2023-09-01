<template>
  <section class="faq">
    <div class="container mx-auto">
      <h2 class="faq_title h2 text-center mb-[50px]">
        Frequently Asked Questions
      </h2>
      <!-- ITEM WRAPPER -->
      <div class="max-w-5xl mx-auto">
        <!-- ITEM -->
        <div class="faq_item px-[30px] pt-7 border-b mb-4 cursor-pointer select-none">
          <!-- TITLE & ICON -->
          <div class="flex items-center justify-between mb-[10px]">
            <!-- TITLE -->
            <h4 class="h4">What services are offered at MedCenter?</h4>
            <!-- ICON -->
            <div class="faq_btn text-accent">
              <i class="ri-add-fill text-2xl"></i>
            </div>
          </div>
          <!-- ANSWER TEXT -->
          <div class="faq_answer h-0 overflow-hidden">
            <p class="font-light">
              We provide a comprehensive range of services including:
              Primary Care: Routine check-ups, preventive care, and management of chronic conditions.
              Specialty Services: Cardiology, dermatology, orthopedics, and more.
              Diagnostic Services: X-rays, MRI, lab tests, and other diagnostic procedures.
              Emergency Care: Immediate care for urgent and emergency medical situations.
              Surgical Services: Minor and major surgeries performed by experienced surgeons.
              Pediatric Care: Healthcare services tailored for children and adolescents.
            </p>
          </div>
        </div>
        <!-- ITEM -->
        <div class="faq_item px-[30px] pt-7 border-b mb-4 cursor-pointer select-none">
          <!-- TITLE & ICON -->
          <div class="flex items-center justify-between mb-[10px]">
            <!-- TITLE -->
            <h4 class="h4">How can I make an appointment?</h4>
            <!-- ICON -->
            <div class="faq_btn text-accent">
              <i class="ri-add-fill text-2xl"></i>
            </div>
          </div>
          <!-- ANSWER TEXT -->
          <div class="faq_answer h-0 overflow-hidden">
            <p class="font-light">
              Making an appointment with our medical center is simple and convenient. You can:
              Call Us: Reach out to our appointment desk at (+51) 43 249 01 during our business hours.
              Online Booking: Use our Online Appointment System to schedule your visit. You can select your preferred date and time, and choose a provider if applicable.
              Walk-In: Visit our center directly. However, we recommend scheduling an appointment in advance to ensure availability.
            </p>
          </div>
        </div>
        <!-- ITEM -->
        <div class="faq_item px-[30px] pt-7 border-b mb-4 cursor-pointer select-none">
          <!-- TITLE & ICON -->
          <div class="flex items-center justify-between mb-[10px]">
            <!-- TITLE -->
            <h4 class="h4">What should I bring to my first appointment?</h4>
            <!-- ICON -->
            <div class="faq_btn text-accent">
              <i class="ri-add-fill text-2xl"></i>
            </div>
          </div>
          <!-- ANSWER TEXT -->
          <div class="faq_answer h-0 overflow-hidden">
            <p class="font-light">
              To ensure a smooth and efficient visit, please bring the following items to your first appointment:
              Identification: A government-issued ID (e.g., driver’s license, passport).
              Insurance Card: Your current health insurance card and any necessary referral forms.
              Medical Records: Any relevant medical records, including previous diagnoses, treatments, and medications.
              List of Medications: A list of current medications, including dosages and frequency.
              Previous Test Results: Copies of any recent diagnostic test results or imaging studies.
            </p>
          </div>
        </div>
        <!-- ITEM -->
        <div class="faq_item px-[30px] pt-7 border-b mb-4 cursor-pointer select-none">
          <!-- TITLE & ICON -->
          <div class="flex items-center justify-between mb-[10px]">
            <!-- TITLE -->
            <h4 class="h4">What are your office hours?</h4>
            <!-- ICON -->
            <div class="faq_btn text-accent">
              <i class="ri-add-fill text-2xl"></i>
            </div>
          </div>
          <!-- ANSWER TEXT -->
          <div class="faq_answer h-0 overflow-hidden">
            <p class="font-light">
              Our medical center is open during the following hours:
              Monday to Thursday: 8:00 AM - 6:00 PM
              Friday to Saturday: 10:00 AM - 4:00 PM
              Sunday: Emergency only/Closed
            </p>
          </div>
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

            sr.reveal('.faq_title', {interval: 200});
            sr.reveal('.faq_item', {interval: 200});

            });
        }
    }
</script>

<style scoped>
/* Your scoped CSS here */
</style>
