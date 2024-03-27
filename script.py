# Placeholder for user data and article data
import asyncio
import os
import json
import dotenv
import openai

from aiconfig import AIConfigRuntime, InferenceOptions, Prompt

user_data = ["{\n  \"userProfile\": {\n    \"age\": 25,\n    \"height\": \"170cm\",\n    \"weight\": \"60kg\",\n    \"bloodType\": \"A+\",\n    \"medicalHistory\": {\n      \"allergies\": [],\n      \"chronicConditions\": [],\n      \"medications\": [],\n      \"surgeries\": []\n    }\n  },\n  \"menstrualCycle\": {\n    \"averageLength\": 28,\n    \"averagePeriodDuration\": 5,\n    \"lastPeriodStartDate\": \"2024-02-10\",\n    \"symptomsTracking\": {\n      \"cramps\": \"moderate\",\n      \"bloating\": \"mild\",\n      \"moodSwings\": \"yes\"\n    }\n  },\n  \"reproductiveHealth\": {\n    \"pregnancies\": 0,\n    \"planningPregnancy\": \"no\",\n    \"contraceptiveUse\": \"yes\",\n    \"typeOfContraceptive\": \"birth control pills\"\n  },\n  \"generalHealth\": {\n    \"diet\": {\n      \"type\": \"balanced\",\n      \"restrictions\": []\n    },\n    \"exerciseFrequency\": \"3 times a week\",\n    \"sleepAverage\": \"8 hours\",\n    \"stressLevel\": \"moderate\",\n    \"alcoholConsumption\": \"socially\",\n    \"smokingHabits\": \"non-smoker\"\n  },\n  \"screeningTests\": {\n    \"lastPapSmear\": \"2023-01-15\",\n    \"lastMammogram\": \"not applicable\",\n    \"lastBoneDensityTest\": \"not applicable\",\n    \"vaccinations\": {\n      \"hpv\": \"completed\",\n      \"tetanus\": \"up to date\"\n    }\n  }\n}\n"] # Add all user data here

article_data = """
Physiology, Menstrual Cycle
Dhanalakshmi K. Thiyagarajan; Hajira Basit; Rebecca Jeanmonod.

Author Information and Affiliations
Last Update: October 24, 2022.

Go to:
Introduction
The reproductive system of a female, unlike men, shows regular cyclic changes that teleologically may be regarded as periodic preparation for pregnancy and fertilization. In primates and humans, the cycle is a menstrual cycle, and its most conspicuous feature is the periodic vaginal bleeding that occurs with the shedding of uterine mucose (menstruation). The length of the cycle is notoriously variable, but an average figure is 28 days from the start of one menstrual period to the start of the next. By common usage, the days of the cycle are identified by number starting with the first day of menstruation. It begins at puberty, ranging from the ages of 10 to 16, and ends at menopause at an average age of 51.[1][2][3]

Go to:
Function
Hormones are secreted in a negative and positive feedback manner to control the menstrual cycle. Hormone secretion begins in the hypothalamus where gonadotropin-releasing hormone (GnRH) is secreted in an increased, pulsatile fashion once puberty starts. GnRH is then transported to the anterior pituitary, where it activates its 7-transmembrane G-protein receptor. This provides a signal to the anterior pituitary to secrete stimulating follicle hormone (FSH) and luteinizing hormone (LH). FSH and LH provide input to the ovaries. Within the ovarian follicle, there are 2 cell types responsible for hormone production, theca cells, and granulosa cells. LH stimulates theca cells to produce progesterone and androstenedione by activating the enzyme, cholesterol desmolase. Once androstenedione is secreted, the hormone diffuses to the nearby granulosa cells. Here, FSH stimulates the granulosa cells to convert androstenedione to testosterone then 17-beta-estradiol by activating the enzyme, aromatase. As levels of 17-beta-estradiol or progesterone increase based on the phases of the menstrual cycle, there is negative feedback back to the anterior pituitary to lower the levels of FSH and LH being produced and subsequently, the levels of 17-beta-estradiol and progesterone produced. An exception to this is during ovulation. In this case, once a critical amount of 17-beta-estradiol is produced, it provides positive feedback to the anterior pituitary to produce increased amounts of FSH and LH. This feedback system is represented in figure 1. Additionally, within the feedback system, the granulosa cells produce inhibin and activin, which inhibit and stimulate FSH release from the anterior pituitary, respectively. This feedback mechanism is controlled by upregulating, to increase hormone production, or downregulating to decrease hormone production, the GnRH receptors on the anterior pituitary.[4][5][6]

Go to:
Mechanism
Phase 1: The Follicular, or Proliferative Phase

The first phase of the menstrual cycle is the follicular or proliferative phase. It occurs from day one to day 14 of the menstrual cycle, based on the average duration of 28 days. The variability in the length of the menstrual cycle occurs due to variations in the length of the follicular phase. The main hormone during this phase is estrogen, specifically 17-beta-estradiol. The increase in this hormone occurs by the upregulation of the FSH receptors within the follicle at the beginning of the cycle. However, as the follicular phase progresses to the end, the increased amounts of 17-beta-estradiol will provide negative feedback to the anterior pituitary. The purpose of this phase is to grow the endometrial layer of the uterus. 17-beta-estradiol achieves this by increasing the growth of the endometrial layer of the uterus, stimulating increased amounts of stroma and glands, and increasing the depth of the arteries that supply the endometrium, the spiral arteries.

Additionally, this phase is also essential to create an environment that is friendly and helpful to possible incoming sperm. 17-beta-estradiol achieves this by creating channels within the cervix, allowing for sperm entry.[7] The channels are made within the abundant, watery, and elasticity changes of the cervical mucous. During this phase, a primordial follicle begins to mature into a Graafian follicle. The surrounding follicles begin to degenerate, which is when the Graafian follicle becomes the mature follicle. This sets up the follicle for ovulation, the next step.

Ovulation

Ovulation always occurs 14 days before menses; therefore, with an average 28-day cycle, ovulation occurs on day 14. At the end of the proliferative phase, 17-beta-estradiol levels are at a high due to the follicle maturation and increased production of the hormone. During this time only, 17-beta-estradiol provides positive feedback for FSH and LH production. This occurs when a critical level of 17-beta-estradiol is reached, at least 200 picograms per milliliter of plasma. The high levels of FSH and LH present during this time is called the LH surge. As a result, the mature follicle breaks, and an oocyte is released. The changes to the cervix as initiated during the follicular phase further increase, allowing for increased, waterier cervical mucous to better accommodate the possible sperm—the levels of 17-beta-estradiol fall at the end of ovulation. 

Phase 2: The Luteal or Secretory Phase

The next phase of the menstrual cycle is the luteal or secretory phase. This phase always occurs from day 14 to day 28 of the cycle. Progesterone stimulated by LH is the dominant hormone during this phase to prepare the corpus luteum and the endometrium for possible fertilized ovum implantation. As the luteal phase ends, progesterone will provide negative feedback to the anterior pituitary to decrease FSH and LH levels and, subsequently, the 17-beta-estradiol and progesterone levels. The corpus luteum is a structure formed in the ovary at the site of the mature follicle rupture to produce 17-beta-estradiol and progesterone, which is predominant at the end of the phase due to the negative feedback system. The endometrium prepares by increasing its vascular supply and stimulating more mucous secretions. This is achieved by the progesterone stimulating the endometrium to slow down endometrial proliferation, decrease lining thickness, develop more complex glands, accumulate energy sources in the form of glycogen, and provide more surface area within the spiral arteries.

Contrary to the cervical mucous changes seen during the proliferative phase and ovulation, progesterone decreases and thickens the cervical mucous making it non-elastic since the fertilization period passed, and sperm entry is no longer a priority. Additionally, progesterone increases the hypothalamic temperature, so body temperature increases during the luteal phase. Near the end of the secretory phase, plasma levels of 17-beta-estradiol and progesterone are produced by the corpus luteum. If pregnancy occurs, a fertilized ovum is implanted within the endometrium, and the corpus luteum will persist and maintain the hormone levels. However, if no fertilized ovum is implanted, then the corpus luteum regresses, and the serum levels of 17-beta-estradiol and progesterone decrease rapidly.

Normal Menstruation

When the hormone levels decrease, the endometrium layer, as it has been changed throughout the menstrual cycle, is not able to be maintained. This is called menses, considered day 0 to day 5 of the next menstrual cycle. The duration of menses is variable. Menstrual blood is chiefly arterial, with only 25% of the blood being venous blood. It contains prostaglandins, tissue debris, and relatively large amounts of fibrinolysis from endometrial tissue. The fibrinolysis lyses the clot so that menstrual blood does not contain clots typically unless the flow is heavy. 

The usual duration of the menstrual flow is 3-5 days, but flows as shorts as 1 day and as long as 8 days can occur in a normal female. The amount of blood loss can range from slight spotting to 80 mL and the average being 30 mL. Loss of more than 80 mL of the blood is considered abnormal. Various factors can affect the amount of blood flow, including medications, the thickness of the endometrium, blood disorders, and disorders of blood clotting, etc.

Go to:
Pathophysiology
Anovulatory Cycles

In some cases, ovulation fails to occur during the menstrual cycle. Such cycles are called anovulatory cycles, and they are common for the first 12-18 months after menarche (The occurrence of the first menstrual period) and again before the onset of menopause. When ovulation does not occur, usually no corpus luteum is found, and the effect of progesterone on the endometrium is absent.[8] Estrogen continues to cause the growth of the endometrium, however, and the proliferative endometrium becomes thick enough to break down and begin to slough. The time it takes for the bleeding to occur is fluctuating, but it generally occurs in less than 28 days from the previous menstrual period. The flow is also inconsistent and ranges from scanty to relatively profuse.[9]

Go to:
Clinical Significance
A female has an average of 450 menses throughout her lifetime; therefore, it is important to understand the menstrual cycle and its physiology because of the various complications, consequences, and distress that it may have for a female patient. A female presenting with primary or secondary amenorrhea will need to undergo clinical testing to diagnose the reason. Still, reasonable testing from the level of the ovaries to the hypothalamus cannot be performed unless a clinician thoroughly understands the hormone feedback system. Additionally, there may be problems with her menses themselves, such as premenstrual syndrome, dysmenorrhea, or menorrhagia. Without an understanding of the female anatomy and menstrual cycle physiology, a clinician would be unable to obtain a complete history and physical to allow understanding of the underlying cause. Infertility is a prominent issue in our society, and the menstrual cycle is the basis for how a woman’s body prepares for pregnancy, so each patient’s menstrual cycle must be evaluated as a possible area of concern for her infertility. As clinicians, we must understand the menstrual cycle in its entirety to provide relevant clinical care to our female patients
"""


dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def save_parameters_to_json(article_data, user_data):
    parameters = {
        "parameters": {
            "article_string": article_data,
            "user_data": user_data
        }
    }
    with open('output_parameters.json', 'w') as json_file:
        json.dump(parameters, json_file, indent=2)

async def main():
    while True:
        user_input = input("\nUser: ")
        if user_input == "quit":
            break

        # Dynamically generate the prompt name and prompt object
        new_prompt_name = (
            f"prompt{len(config.prompts)+1}"  # Prompt{number of prompts}
        )
        new_prompt = Prompt(name=new_prompt_name, input=user_input)

        # Add the new prompt and run the model
        config.add_prompt(new_prompt.name, new_prompt)
        await config.run(new_prompt_name, options=inference_options)

        save_parameters_to_json(article_data, user_data)


if __name__ == "__main__":
    inference_options = InferenceOptions()
    config = AIConfigRuntime.load("testing.json")
    asyncio.run(main())



# # Modify the function to be async and use await for the run method
# async def personalize_articles(user_data, article_data):\

#     config = AIConfigRuntime.load('testing.json')

#     config.set_parameter("user_data", "${user_data}")
#     config.set_parameter("article_string", "${article_data}")


#     # await config.run()

#     results =  await config.run("article_analysis")  # Use await here

#     print('resutlt', results)

#     config.save()

#     # inputs = {
#     #     'user_data': json.dumps(user_data),
#     #     'article_string': article_data
#     # }
    

#     personalized_article = results
    
#     return personalized_article



# if __name__ == "__main__":
#     filename = "all_personalized_articles.txt"

#     # Run the async function and wait for the result
#     async def main():
#         personalized_article = await personalize_articles(user_data, article_data)
#         return personalized_article

#     # Run the main coroutine and capture the result
#     personalized_article_result = asyncio.run(main())
    
#     # Write the result to a TXT file
#     with open(filename, 'w') as txt_file:
#         # Assuming personalized_article_result is a string or can be converted to a string
#         txt_file.write(str(personalized_article_result))

#     print(f"All personalized articles have been written to {filename}")
