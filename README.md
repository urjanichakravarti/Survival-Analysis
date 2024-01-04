# Survival Analysis 

## Objective
Survival Analysis is a branch of statistics for analyzing the expected duration of time until one event occurs. This event could be anything, like the death of a person, loss of a customer, failure of a course, and  failure in mechanical systems. 
In this project, we have extended the applications of Survival Analysis in the education and healthcare industries. 

**Education Problem Statement:**  To predict whether a student will withdraw from a course or university based on past/present behavior or other parameters. Identifying these factors can help us to prevent students from withdrawing from courses. 

**Healthcare Problem Statement:** To analyze and predict the effect a certain medicine/parameter has on the patient's survival rate. This can help us to reduce patient mortality. 

## Data Source 

The <a href="https://analyse.kmi.open.ac.uk/open_dataset">Open University Learning Analytics Dataset</a> contains data about courses, students, and their assessments for seven selected courses (called modules). Presentations of courses start in February and October - they are marked by “B” and “J” respectively. The dataset consists of tables connected using unique identifiers. The datasets can be found inside the 'Data Files' directory.

**courses.csv**
* `code_module` – code name of the module, which serves as the identifier.
* `code_presentation` – code name of the presentation. It consists of the year and “B” for the presentation starting in February and “J” for the presentation starting in October.
* `length` - length of the module-presentation in days.

**assessments.csv**
* `code_module` – identification code of the module, to which the assessment belongs.
* `code_presentation` - identification code of the presentation, to which the assessment belongs.
* `id_assessment` – identification number of the assessment.
* `assessment_type` – type of assessment. Three types of assessments exist: Tutor Marked Assessment (TMA), Computer Marked Assessment (CMA) and Final Exam (Exam).
* `date` – information about the final submission date of the assessment calculated as the number of days since the start of the module-presentation. The starting date of the presentation has number 0 (zero).
* `weight` - weight of the assessment in %. Typically, Exams are treated separately and have the weight 100%; the sum of all other assessments is 100%.

**studentInfo.csv**
* `code_module` – an identification code for a module on which the student is registered.
* `code_presentation` - the identification code of the presentation during which the student is registered on the module.
* `id_student` – a unique identification number for the student.
* `gender` – the student’s gender.
* `region` – identifies the geographic region, where the student lived while taking the module-presentation.
* `highest_education` – highest student education level on entry to the module presentation.
* `imd_band` – specifies the Index of Multiple Depravation band of the place where the student lived during the module-presentation.
* `age_band` – band of the student’s age.
* `num_of_prev_attempts` – the number times the student has attempted this module.
* `studied_credits` – the total number of credits for the modules the student is currently studying.
* `disability` – indicates whether the student has declared a disability.
* `final_result` – student’s final result in the module-presentation.

**studentRegistration.csv**
* `code_module` – an identification code for a module.
* `code_presentation` - the identification code of the presentation.
* `id_student` – a unique identification number for the student.
* `date_registration` – the date of student’s registration on the module presentation, this is the number of days measured relative to the start of the module-presentation (e.g. the negative value -30 means that the student registered to module presentation 30 days before it started).
* `date_unregistration` – date of student unregistration from the module presentation, this is the number of days measured relative to the start of the module-presentation.

The <a href="https://dmkd.cs.vt.edu/projects/survival/data/">Survival Package</a> in R contains the data for colon and ovarian cancer, among other datasets. In the case of colon cancer, the data is from one of the first successful trials of adjuvant chemotherapy for colon cancer.  For ovarian cancer, we predict survival in a randomized trial comparing two treatments for ovarian cancer. The datasets can be found inside the 'Data Files' directory.

**colon.csv**
* `id` - id
* `study` - 1 for all patients
* `rx` - Treatment - Obs(ervation), Lev(amisole), Lev(amisole)+5-FU
* `sex` -  1=male
* `age` - in years
* `obstruct` - obstruction of colon by tumour
* `perfor` - perforation of colon
* `adhere` - adherence to nearby organs
* `nodes` - number of lymph nodes with detectable cancer
* `time` - days until event or censoring
* `status` - censoring status
* `differ` - differentiation of tumour (1=well, 2=moderate, 3=poor)
* `extent` - Extent of local spread (1=submucosa, 2=muscle, 3=serosa, 4=contiguous structures)
* `surg` - time from surgery to registration (0=short, 1=long)
* `node4` - more than 4 positive lymph nodes
* `etype` event type: 1=recurrence,2=death

**ovarian.csv**
* `futime` - survival or censoring time
* `fustat` - censoring status
* `age` - in years
* `resid.ds` - residual disease present (1=no,2=yes)
* `rx` - treatment group
* `ecog.ps` - ECOG performance status (1 is better, see reference)

## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/urjanichakravarti/Survival-Analysis.git
   ```

2. Install required libraries. Each file contains the analysis of one problem. Run the files to obtain results.
