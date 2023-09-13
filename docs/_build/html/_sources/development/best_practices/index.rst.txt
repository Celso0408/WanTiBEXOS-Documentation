Best Practices for **WaNo** development
#######################################

- To starting a new **WaNo** for the first time, download one,  copy it into the local repository, and modify it according
  to the simulation needs. This will speed up the development process.

- The majority of the scientific packages have a considerable number of parameters, which the end-user may, in principle,
  change. However, only a small subset of parameters is significant for the particular simulation protocol for reoccurring
  user cases. Thus, it worth spend a bit of time to select this subset of parameters.

- In developing a new **WaNo**, we need to clarify what parameters we need to vary in the protocol and only include
  those into the **WaNo**, the remaining we keep fixed in the input files. This decreases the chances of mistakes.

- Depending on the tool/case, it may be beneficial to provide several separate **WaNos** for one workflow. Adaptions
  to the **WaNo** to allow more flexibility are a matter of minutes.

- Always prefer to read the inputs parameters from the ``rendered_wano.yml`` file. This will avoid overpopulating the **WaNo** ``.xml`` file.
