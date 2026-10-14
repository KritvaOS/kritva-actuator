# Kritva Smart Actuator Development Platform

## Internal Training and Engineering Reference

**Document type:** Internal project README and training reference\
**Project:** KritvaOS Smart Actuator Development Platform\
**Target prototype:** Low-voltage rotary joint\
**Team:** One Electronics/Electrical Engineering Intern and one
Mechanical Engineering Intern\
**Planning duration:** 12 weeks\
**Status:** Initial project baseline --- performance requirements and
component choices are not yet frozen

------------------------------------------------------------------------

> **Current engineering focus:** A0 = safe, measured closed-loop bench
> prototype (₹10k--₹15k planning target). A1 = reusable, documented
> smart-actuator module (₹20k--₹30k cumulative planning target). These
> budgets are estimates; torque/speed/current/thermal limits must be
> verified before procurement. See **A0/A1 Engineering Baseline ---
> Highlighted Requirements** below.

## Project Artwork

The following concept infographic provides a visual overview of the
actuator architecture, development stages, humanoid-joint applications,
and reference projects. It is an illustrative concept---not a released
mechanical design or a validated bill of materials.

![Kritva Smart Actuator --- concept
overview](docs/images/kritva-smart-actuator-overview.png)

> **Engineering note:** Use this artwork for project orientation and
> training. Do not use its illustrative geometry, component placement,
> or depicted architecture as manufacturing data. Freeze the real motor,
> gearbox, encoder, mounting interfaces, electrical limits, and safety
> requirements through the project design process.

### Actuator family and preliminary parameter map

This second infographic visualizes the proposed S/M/L actuator family
and a preliminary parameter envelope. **The numerical values shown in
the artwork are illustrative placeholders for discussion, not approved
requirements, verified capabilities, or purchasing specifications.** Use
the controlled tables below for project planning, and replace
provisional values only after calculations, supplier verification, and
design review.

![Kritva Smart Actuator --- actuator family and preliminary
specification
concept](docs/images/kritva-smart-actuator-family-and-baseline.png)

## 1. Project Purpose

The Kritva Smart Actuator Development Platform is an educational
engineering project intended to produce a low-cost rotary actuator
prototype that can evolve into a reusable smart actuator for future
KritvaOS humanoid-robot systems.

The project will combine commercially available mechanical components
with in-house electronics, firmware, mechanical integration, validation,
and software interfaces.

The first prototype is intended for a securely mounted bench fixture. It
is not automatically suitable for installation on a humanoid robot or
for human-interactive use.

### Primary objectives

1.  Learn and validate BLDC/PMSM motor control using an established
    development platform.
2.  Integrate a commercial motor, off-the-shelf gearbox, and
    output-position encoder.
3.  Develop and document a practical mechanical assembly.
4.  Progress toward an in-house MCU controller and reusable firmware.
5.  Define a stable actuator command/state interface that can later
    integrate with KritvaOS and Kritva Edge.
6.  Measure actual cost and performance before making claims about
    production economics.

### Guiding principle

**Build a low-cost prototype first, but structure the design so that the
work can be reused.** Do not optimize for minimum component cost at the
expense of safe operation, measurable performance, or clear
documentation.

------------------------------------------------------------------------

## 2. Scope and Non-Goals

### In scope

-   One low-voltage rotary actuator prototype.
-   Commercial BLDC/PMSM motor.
-   Off-the-shelf planetary gearbox for the initial design, subject to
    requirements review.
-   Output-shaft encoder.
-   Commercial motor-control development board for initial bring-up.
-   FOC implementation or adaptation using a suitable established
    codebase.
-   Closed-loop position control; velocity and torque control only where
    supported and validated.
-   Mechanical CAD, fabrication, assembly, and characterization.
-   Basic host communication; CAN is the target for the smart-actuator
    stage.
-   Fault handling, test evidence, and engineering documentation.
-   A custom controller PCB may be designed after the initial
    motor-control system is validated.

### Out of scope for the first prototype

-   Designing and manufacturing a motor from raw materials.
-   Manufacturing a precision harmonic-drive gearbox.
-   Developing a production-ready or safety-certified actuator.
-   Operating the prototype on a loaded humanoid robot.
-   Claiming reliable collision detection from motor current alone.
-   Guaranteeing that prototype cost equals eventual production cost.

------------------------------------------------------------------------

## 3. Development Releases

### A0 --- Educational Motor-Control Prototype

**Purpose:** Validate the motor, feedback, and control approach before
investing in custom electronics.

Expected work: - Select a suitable development board and motor. - Bring
up motor and encoder interfaces. - Establish safe, current-limited
operation. - Implement or adapt FOC. - Demonstrate closed-loop position
control. - Record current, temperature, tracking error, and
repeatability where measurable. - Document limitations and operating
limits.

**Indicative budget target:** ₹10,000--₹15,000. This is a planning
target, not a supplier-verified quotation.

**Exit gate:** Repeatable bench operation with documented limits and
test evidence.

### A1 --- Reusable Smart Actuator

**Purpose:** Integrate the motor, gearbox, output encoder, mechanical
assembly, controller, and firmware.

Expected work: - Finalize the mechanical package. - Validate the output
encoder mounting and alignment. - Implement diagnostics and defined
fault responses. - Design a custom controller PCB if A0 results justify
it. - Characterize output torque and speed using suitable test
equipment. - Document the bill of materials, assembly, and measured
performance.

**Indicative cumulative budget target:** ₹20,000--₹30,000. Actual cost
depends on component choices, fabrication, test equipment, and rework.

**Exit gate:** Integrated prototype passes approved mechanical,
electrical, and firmware tests.

### A2 --- KritvaOS Integration

**Purpose:** Provide a documented actuator interface suitable for
integration with Kritva Edge and higher-level KritvaOS software.

Expected work: - Define command, feedback, diagnostic, and fault
semantics. - Implement CAN communication where supported by selected
hardware. - Provide a host-side demonstration and/or driver. - Add
command validity, timeout, and communication-health handling. - Test
using a simulated actuator before relying on physical hardware. -
Document integration limitations and future work.

**Exit gate:** A host application can command the actuator through the
documented interface, observe state, and handle specified faults.

The release gates are planning targets. They do not establish that the
actuator is safe for human-interactive operation.

------------------------------------------------------------------------

## 24-Week Development Plan --- Parallel Workstreams

### Planning principle

The 24-week schedule is designed around component lead time and
iteration. Procurement is not treated as idle time: the electronics
intern can progress with controller evaluation, firmware and test
infrastructure, while the mechanical intern develops CAD, interfaces,
fabrication drawings and fixture concepts. Both interns converge when
the selected components arrive.

The schedule assumes one electronics/firmware intern, one mechanical
intern, and a project lead who approves requirements, purchasing, safety
gates and design decisions. Supplier lead times can vary; re-plan if
actual delivery dates change. A custom PCB is optional and must not
block the first closed-loop demonstration.

![Kritva Smart Actuator --- 24-week parallel development
roadmap](docs/images/kritva-smart-actuator-24-week-roadmap.png)

### Workstream plan

  ---------------------------------------------------------------------------------------------------------------
  Weeks          Shared / project Electronics & firmware intern    Mechanical intern           Parallel output /
                 lead                                                                          gate
  -------------- ---------------- -------------------------------- --------------------------- ------------------
  1--2           Define use case, Draft electrical block diagram,  Envelope study, joint loads **M1: Requirements
                 target joint,    controller selection criteria,   assumptions, concept        baseline frozen**;
                 safety boundary, motor/encoder interface          layouts, fixture concepts   unknowns and
                 measurable       checklist                                                    owners recorded
                 requirements and                                                              
                 budget                                                                        

  3--4           Joint review of  Compare development boards,      Compare gearbox/motor       **M2: Components
                 motor, gearbox,  motor-control libraries,         dimensions, preliminary     ordered**; lead
                 encoder and      interface and current/voltage    CAD, mounting and cable     times and
                 controller       limits; build software/toolchain routing                     substitutes
                 compatibility;                                                                tracked
                 place orders                                                                  
                 only after                                                                    
                 approval                                                                      

  5--6           Track supplier   Read datasheets; prepare         Detailed CAD with envelope  Design work
                 delivery and     firmware skeleton, encoder       placeholders,               continues while
                 review design    decoding tests, command/logging  shaft/mounting concepts,    parts are in
                 assumptions      harness, safe power-up checklist basic strength/clearance    transit
                                                                   review                      

  7--8           Review component Bench-evaluate                   Release prototype           **M3: Mechanical
                 arrival and      controller/software using vendor CAD/drawings for 3D         design ready for
                 compatibility;   examples or simulator where      printing or machining;      prototype
                 resolve          available; prepare motor         build/inspect test fixture  fabrication**
                 procurement gaps bring-up and data logging                                    

  9--10          Safety review    Bring up controller with current Fabricate                   Mechanical
                 and controlled   limits; verify communication,    housing/brackets/fixture;   fabrication and
                 initial power-up encoder and motor phases as      inspect fit, fasteners,     electrical
                 approval         components permit                clearances and cable exits  bring-up proceed
                                                                                               in parallel

  11--12         Joint            Motor                            Fit motor, gearbox and      **M4: A0 prototype
                 integration      identification/configuration,    encoder; verify alignment,  demonstration**;
                 review; log      initial FOC where supported,     backlash and serviceability if parts are late,
                 issues and       bounded open-loop tests, then    without powered operation   use a revised
                 decide           closed-loop position control     where appropriate           gate, not unsafe
                 corrective                                                                    shortcuts
                 actions                                                                       

  13--14         Review A0        Tune position loop; measure      Revise CAD from actual      A0 report and A1
                 measurements and tracking/repeatability/current   dimensions; make assembly   design review
                 decide what must and temperature where available; drawing, BOM and build      
                 change for A1    improve fault handling           notes                       

  15--16         Approve A1       Define reusable                  Manufacture/rework          **M5: A1
                 configuration    firmware/configuration and       integrated housing and      mechanical
                 and scope;       diagnostics; optional PCB        mounting; prepare assembly  assembly ready**
                 decide whether   schematic/layout only if         and cable-management        
                 custom PCB is    schedule and budget allow        details                     
                 justified                                                                     

  17--18         Coordinate       Integrate controller, output     Assemble module; inspect    First integrated
                 integration and  feedback, logging and            fasteners, alignment,       A1 build
                 keep interface   communication interface; CAN may encoder mount, cable        
                 decisions        remain a target if hardware/time protection and thermal      
                 controlled       is insufficient                  clearances                  

  19--20         Review           Regression tests, bounded motion Mechanical checks,          **M6: A1
                 functional and   tests, timeout/fault tests where backlash/repeatability      functional
                 safety evidence; supported; capture logs          checks and safe load        validation**
                 prioritize                                        testing only with           
                 defects                                           appropriate                 
                                                                   fixture/instrumentation     

  21--22         Review           Characterize control response,   Characterize speed,         **M7: Performance
                 performance data current and temperature under    backlash, vibration/noise   characterization
                 and remaining    defined test conditions;         and mechanical              complete**
                 risks            document limits                  repeatability; refine       
                                                                   assembly if needed          

  23--24         Final review,    Release firmware/configuration,  Release CAD/drawings, BOM,  **M8: A1 release
                 unresolved risks wiring/pinout, test scripts and  assembly procedure and      package and demo**
                 and next-stage   known limitations                mechanical test results     
                 decision                                                                      
  ---------------------------------------------------------------------------------------------------------------

### Work that can proceed before components arrive

**Electronics / firmware** - Read controller and motor datasheets;
verify supported motor types and voltage/current limits. - Set up
compiler, SDK, firmware repository, coding rules and build/test
workflow. - Prepare encoder and command-interface abstractions with
mocked or simulated inputs. - Create logging format and scripts for
position, velocity, current, temperature and fault state. - Draft safe
power-up, current-limit and emergency-stop procedures. - Build a
motor/controller compatibility matrix and procurement checklist.

**Mechanical** - Create envelope CAD using clearly marked placeholder
dimensions. - Design a modular mounting plate, guarded bench fixture and
cable-routing provisions. - Develop parametric CAD so the housing can be
updated quickly when actual parts arrive. - Prepare drawing templates,
fastener/BOM conventions and assembly inspection checklist. - Analyze
the selected joint concept and record assumptions; do not freeze
critical interfaces until datasheets arrive.

**Shared** - Agree interface-control document (motor shaft, gearbox
input/output, encoder location, connectors, mounting datums). - Maintain
a decision log, risk/issue list, procurement tracker and change
history. - Review the same updated datasheets together before final CAD
and wiring are released.

### Milestones and exit gates

-   **M1 / Week 2 --- Requirements frozen:** use case, test conditions,
    safety limits, target performance and TBD owners documented.
-   **M2 / Week 4 --- Procurement released:** compatible component set
    approved; orders and lead times recorded.
-   **M3 / Week 8 --- Design ready:** CAD and bring-up plan ready for
    actual component dimensions.
-   **M4 / Week 12 --- A0 demonstration target:** bounded closed-loop
    position control and output feedback demonstrated, or re-baselined
    transparently if supply delays prevent it.
-   **M5 / Week 16 --- A1 assembly ready:** integrated mechanical design
    and assembly plan approved.
-   **M6 / Week 20 --- A1 functional validation:** repeatable motion and
    agreed basic fault/timeout tests evidenced.
-   **M7 / Week 22 --- Characterization:** measured performance and
    operating limits documented.
-   **M8 / Week 24 --- Release review:** reproducible demo, BOM, CAD,
    wiring, firmware/configuration, test evidence and open-issue list
    delivered.

### Schedule controls

1.  Track supplier lead time and order status weekly; identify
    alternates before a delay becomes critical.
2.  Freeze only the interfaces supported by evidence. Keep placeholder
    dimensions and provisional requirements visibly marked.
3.  Do not start final machining from placeholder CAD.
4.  A custom controller PCB is optional; if it threatens the schedule,
    complete A1 on the development board and document the PCB as
    follow-on work.
5.  If parts are late, continue documentation, software abstractions,
    fixture work and test preparation. Move the affected integration
    gate instead of bypassing safety or acceptance checks.
6.  No loaded humanoid or human-interactive use is authorized by this
    development plan; testing remains on a secured bench fixture until a
    separate safety and system validation process approves more.

------------------------------------------------------------------------

## A0/A1 Engineering Baseline --- Highlighted Requirements

> **Priority for the current internship:** A0 and A1 are the active
> scope. S/M/L actuator bands are future planning concepts and must not
> distract the team from completing one safe, measured prototype first.

### A0 --- Educational Motor-Control Prototype

**Goal:** Demonstrate repeatable, closed-loop position control on a
low-voltage bench fixture using commercially available components and a
development controller.

  -----------------------------------------------------------------------
  Parameter               A0 baseline / target    Acceptance evidence
  ----------------------- ----------------------- -----------------------
  Prototype scope         One rotary joint on a   Photos, assembly notes,
                          rigid bench fixture; no fixture inspection
                          humanoid installation   

  Motor                   Commercial BLDC/PMSM,   Datasheet and
                          selected with matching  compatibility record
                          controller support      

  Motor controller        Commercial development  Configuration, firmware
                          board; FOC if supported revision, bring-up log
                          by selected             
                          hardware/software       

  Supply class            Prefer 12--24 V DC for  Approved power budget
                          initial selection;      and documented limits
                          actual voltage set by   
                          chosen motor/controller 

  Gearbox                 Off-the-shelf planetary Ratio, rated torque,
                          gearbox, if suitable    efficiency, backlash
                          for the selected        and load data recorded
                          motor/load              

  Position sensing        Output-shaft encoder    Resolution/interface,
                          preferred               mounting, calibration
                                                  and direction test

  Required control mode   Closed-loop             Repeatable
                          output-position control command-and-measure
                                                  test

  Optional modes          Velocity or             Explicitly documented
                          torque/current command  as pass/fail or
                          only if supported and   deferred
                          safe                    

  Communication           Local wired/USB/UART    Reproducible host
                          bring-up initially; no  command/log procedure
                          dependency on CAN for   
                          first motion            

  Telemetry               Position, velocity if   Logs with units,
                          available, motor        sampling details and
                          current if measurable,  known limitations
                          fault state;            
                          temperature where       
                          sensors exist           

  Initial test limits     Conservative current,   Written limits and
                          speed, travel and       verified stop procedure
                          run-time limits; hard   
                          stop or travel guard as 
                          appropriate             

  Safety                  Current-limited supply, Signed bench-test
                          secured fixture,        checklist
                          guarded rotating parts, 
                          accessible power        
                          disconnect; no          
                          human-interactive use   

  Cost target             ₹10,000--₹15,000 for A0 Itemized actual BOM and
                                                  receipts/quotes

  Schedule target         Early milestone within  Milestone review and
                          the 24-week plan        issue log
  -----------------------------------------------------------------------

**A0 exit gate:** The team can command a bounded position move, observe
the output encoder, stop safely, and repeat the test with recorded
results. Document tracking error, repeatability, current, temperature
where available, fault behavior, test conditions, and limitations. If
quantitative accuracy targets have not yet been derived from the
application, report measured values instead of inventing a pass
threshold.

### A1 --- Reusable Smart Actuator

**Goal:** Turn the proven A0 setup into a documented, serviceable
actuator module with a defined mechanical/electrical interface and a
credible path to KritvaOS integration.

  ------------------------------------------------------------------------------------
  Parameter          A1 baseline / target                    Acceptance evidence
  ------------------ --------------------------------------- -------------------------
  Assembly           Integrated motor, gearbox, output       Assembly drawing,
                     encoder, controller and                 interface drawing, photos
                     housing/mounting arrangement            

  Controller         Continue with development board unless  Decision record with
  hardware           evidence justifies a custom PCB; custom cost, risk and schedule
                     PCB is not a mandatory A1 gate          trade-off

  Control            Reusable closed-loop position control;  Regression tests and
                     other modes only where validated        configuration record

  Communication      Define the actuator interface; target   Interface specification,
                     CAN for integration, but keep CAN       message map, timeout
                     bring-up separate from basic            behavior and test log
                     motor-control success                   

  Diagnostics        Expose available                        Example logs and
                     position/velocity/current/temperature   documented unavailable
                     data plus fault/health state            signals

  Fault behavior     Define safe response to command         Fault-injection or
                     timeout, encoder fault, overcurrent and simulated test evidence;
                     overtemperature where hardware supports limitations recorded
                     detection                               

  Mechanical design  Serviceable housing, repeatable         CAD, fabrication drawings
                     mounting datums, protected cable        and assembly procedure
                     routing, access for assembly and        
                     maintenance                             

  Characterization   Measure achievable output speed,        Test report with
                     tracking/repeatability, backlash,       conditions, instruments,
                     current and temperature; torque test    results and
                     only with an appropriate fixture and    uncertainty/limitations
                     measurement method                      

  Power/thermal      Publish verified operating limits and   Datasheet-style prototype
  limits             test stop conditions                    specification

  Cost target        ₹20,000--₹30,000 cumulative A0+A1       Actual BOM separating
                     planning target                         one-time tools from
                                                             per-unit parts

  Documentation      BOM, wiring diagram, pinout,            Documentation review
                     configuration, firmware revision,       checklist
                     bring-up, calibration and               
                     troubleshooting                         

  Schedule target    Complete within the 24-week plan, with  Milestone review and
                     custom PCB allowed to defer             deferred-items list
  ------------------------------------------------------------------------------------

**A1 exit gate:** Another engineer can assemble or inspect the module,
configure it, run the documented bench test, read status/diagnostics,
understand the operating limits, and reproduce the recorded results
without relying on undocumented knowledge from the original developer.

### A0 vs A1 --- scope boundary

  -----------------------------------------------------------------------
  Capability              A0                      A1
  ----------------------- ----------------------- -----------------------
  Primary objective       Prove motor control and Make the prototype
                          output feedback         reusable and documented

  Mechanical integration  Simple fixture / basic  Integrated, serviceable
                          mounting                mechanical assembly

  Controller              Commercial development  Development board by
                          board                   default; custom PCB
                                                  only if justified

  Position loop           Required                Required,
                                                  regression-tested

  CAN                     Not required for        Target interface for
                          initial motion          future integration;
                                                  implementation depends
                                                  on schedule

  Diagnostics             Basic observations and  Defined status/fault
                          logs                    interface and
                                                  documented limits

  Characterization        Basic tracking,         Broader speed,
                          repeatability, current  backlash, thermal and
                          and temperature where   mechanical
                          available               characterization

  Safety                  Controlled bench test   Controlled bench test
                          only                    only; still not
                                                  approved for
                                                  human-interactive or
                                                  loaded humanoid use

  Deliverable             Working, measured       Reusable actuator
                          educational prototype   module with drawings,
                                                  BOM, interface and test
                                                  evidence
  -----------------------------------------------------------------------

### Requirements that remain TBD

Do not guess values for maximum current, exact speed, tracking-error
tolerance, continuous torque, peak-torque duration, thermal limit, or
CAN update rate before selecting components and defining the intended
test conditions. Assign an owner and due milestone to each TBD, and
close it through calculation, datasheet evidence, or measurement.

------------------------------------------------------------------------

## 4A. Baseline Specification and Parameter Plan

### Status and interpretation

This section establishes a **starting baseline for requirements work**,
not a frozen actuator design. The team must not order parts solely from
the ranges below. Final values depend on the target robot, joint
geometry, payload, motion profile, thermal duty cycle, and verified
supplier data.

The first prototype is one low-voltage, securely mounted bench joint.
The S/M/L family is a future platform direction; A0/A1 are not required
to implement all three sizes.

### A. Initial A0/A1 prototype baseline

  -----------------------------------------------------------------------
  Parameter               Initial planning        Status / verification
                          baseline                
  ----------------------- ----------------------- -----------------------
  Prototype type          Single rotary joint on  Baseline direction
                          a rigid bench fixture   

  Motor                   Commercial BLDC/PMSM    Select after
                                                  torque-speed and
                                                  voltage review

  Motor control           Commercial development  Verify board, firmware,
                          board initially; FOC    motor compatibility
                          where supported         

  Supply voltage          Prefer a low-voltage    Provisional; final
                          12--24 V class for      supply and limits
                          initial bench work      depend on selected
                                                  hardware

  Gearbox                 Off-the-shelf planetary Candidate direction;
                          gearbox                 verify ratio,
                                                  rated/peak torque,
                                                  efficiency, backlash,
                                                  radial/axial load, and
                                                  service life

  Position feedback       Output-shaft encoder,   Resolution, accuracy,
                          preferably magnetic if  mounting, and interface
                          suitable                TBD

  Control objective       Closed-loop             Required A0
                          output-position control demonstration

  Additional modes        Velocity and            Not assumed by default
                          torque/current command  
                          modes only if supported 
                          and validated           

  Communication           Local wired bring-up    CAN
                          first; CAN is the       transceiver/protocol
                          target for the reusable and bus timing TBD
                          smart-actuator stage    

  Monitoring              Current and available   Sensor availability and
                          temperature             accuracy depend on
                          measurements; position, hardware
                          velocity, fault state   

  Mechanical package      Modular housing,        CAD and drawings
                          serviceable assembly,   required
                          protected wiring,       
                          defined mounting datums 

  Prototype environment   Current-limited,        Mandatory project
                          guarded bench test; no  boundary
                          human-interactive or    
                          loaded-humanoid use     

  Cost target A0          ₹10,000--₹15,000        Planning estimate only

  Cumulative cost target  ₹20,000--₹30,000        Planning estimate only
  A1                                              

  Schedule                12 weeks                Planning target
  -----------------------------------------------------------------------

### B. Proposed future actuator family --- discussion envelope only

These broad bands help the team compare possible variants. They are
**not performance commitments**. Torque and speed are coupled by motor
capability, gearing, efficiency, voltage, thermal limits, and duty
cycle; the extremes in a row must not be assumed to be simultaneously
achievable.

  -----------------------------------------------------------------------
  Parameter         Kritva-S (Small)  Kritva-M (Medium) Kritva-L (Large)
  ----------------- ----------------- ----------------- -----------------
  Intended          Wrist, neck,      Elbow, shoulder   Hip, knee, ankle
  application       light joints      auxiliary axes    or other
                                                        high-load axes

  Indicative        2--5 N·m          5--20 N·m         20--80 N·m
  continuous output                                     
  torque band                                           

  Indicative peak   5--10 N·m         20--40 N·m        80--150 N·m
  output torque                                         
  band                                                  

  Indicative        50--300 rpm       30--200 rpm       20--120 rpm
  output-speed                                          
  exploration band                                      

  Possible supply   12--24 V          24--48 V          24--48 V
  class to evaluate                                     

  Indicative        5:1--20:1         10:1--40:1        20:1--100:1
  gearbox-ratio                                         
  exploration                                           

  Outer diameter    40--60 mm         60--90 mm         90--130 mm
  concept                                               

  Length concept    50--80 mm         80--120 mm        120--180 mm

  Mass concept      0.3--0.6 kg       0.6--1.5 kg       1.5--3.5 kg

  Status            Unvalidated       Unvalidated       Unvalidated
                    planning envelope planning envelope planning envelope
  -----------------------------------------------------------------------

**Important:** The torque, speed, voltage, size, and mass bands above
are deliberately provisional. They may prove inappropriate for the
eventual robot. Do not use them for procurement, safety analysis, or
claims of actuator capability. In particular, peak torque needs a
specified duration and thermal recovery condition, and continuous torque
needs a defined duty cycle and cooling assumption.

### C. What should be common across S/M/L

Aim to standardize the platform interfaces, while allowing motor,
inverter, gearbox, housing, and connector current rating to scale.

1.  **Software contract:** consistent command, state, diagnostic, and
    fault semantics.
2.  **Communication:** a common CAN-based application protocol once
    selected; define node identity, units, scaling, update rates,
    timeout behavior, and versioning.
3.  **Control concepts:** shared firmware architecture and test suite,
    with variant-specific parameters and hardware abstraction.
4.  **Feedback semantics:** position, velocity, current, temperature
    (where available), and health/fault state with documented units and
    validity.
5.  **Configuration:** versioned per-variant configuration containing
    motor parameters, encoder calibration, gear ratio, limits, and
    supported modes.
6.  **Mechanical conventions:** standardize datums, fasteners, service
    access, cable routing, and mounting patterns where practical; do not
    require identical external dimensions.
7.  **Validation:** common test procedures and evidence format, with
    variant-specific torque, speed, thermal, backlash, and load tests.

### D. Required engineering decisions before parts are ordered

Record the following in a requirements/decision document and obtain a
cross-workstream review:

-   Target robot mass, payload, limb lengths, and joint range of motion.
-   Per-joint continuous and peak torque, peak duration, output speed,
    acceleration, and duty cycle.
-   Supply voltage, current limits, power budget, connector and cable
    ratings.
-   Gearbox ratio, efficiency, backlash, load ratings, and allowable
    output loads.
-   Output encoder resolution, accuracy, mounting, and calibration
    approach.
-   Thermal limits, cooling assumptions, operating environment, and test
    stop conditions.
-   Mechanical envelope, mass budget, mounting datums, shaft/bearing
    arrangement, and cable exit.
-   Supported command modes and behavior on stale commands, sensor
    errors, overcurrent, overtemperature, and communication loss.
-   Actual supplier quotations, lead times, datasheets, licenses, and
    component compatibility.
-   Test fixture, guarding, emergency power disconnect, and approved
    bench-test procedure.

### E. Sizing method

For each joint, estimate the required output torque from the robot's
static load and intended motion, then add justified dynamic and
uncertainty margins. Check both continuous and peak cases. Estimate
output speed from the joint motion profile. Select motor and gear ratio
using the motor torque-speed curve, gearbox efficiency, thermal limits,
and inverter capability. Verify the result with supplier data and a safe
test fixture.

A rough first-order relationship is:

`output torque ≈ motor torque × gear ratio × gearbox efficiency`

This does not account for all dynamic, thermal, friction, or transient
effects. It is a sizing aid, not a substitute for a full engineering
calculation and validation.

### F. Baseline freeze gate

The baseline is considered ready for procurement only when: - The
requirement values and assumptions are documented with units. -
Electronics and mechanical owners jointly approve interface
compatibility. - Supplier datasheets and quotations support the selected
operating point. - Safety limits and bench-test procedure are
reviewed. - TBDs that could invalidate component selection are closed or
explicitly accepted as risks.

Until this gate passes, mark component values **TBD / provisional** and
do not present the S/M/L bands as finalized specifications.

------------------------------------------------------------------------

## 4. System Overview

Conceptual control path:

``` text
Host / KritvaOS application
          |
          | Joint command
          v
Actuator interface / communication
          |
          v
MCU motor controller
  - Command validation
  - Position/velocity control as supported
  - FOC/current control
  - Diagnostics and limits
          |
          v
Motor driver / three-phase inverter
          |
          v
BLDC/PMSM motor
          |
          v
Gearbox
          |
          v
Output shaft / rotary joint
          |
          v
Output-position encoder
          |
          +------ Feedback to controller
```

This is a conceptual architecture, not a finalized electrical schematic
or software API.

### Important control distinction

A motor-control board may close the fast current loop locally. A host or
Kritva Edge controller may send higher-level position, velocity, or
torque setpoints, depending on the chosen hardware and firmware. Do not
assume every control mode is supported until it is verified on the
selected platform.

The output encoder measures joint position after the gearbox. It does
not remove mechanical backlash; it provides feedback that helps the
controller measure actual output motion.

------------------------------------------------------------------------

## 5. Team and Workstream Ownership

### ACT-01 --- Electronics / Electrical: Motor Control and Firmware

Primary ownership: - Evaluate MCU and motor-control development
boards. - Motor and encoder electrical bring-up. - FOC implementation or
adaptation. - Current and temperature monitoring where supported. -
Closed-loop position control. - Configurable operating limits. -
Diagnostic and fault-handling firmware. - Host communication and CAN
evaluation. - Custom controller schematic/PCB after A0 validation, if
feasible. - Firmware tests and electrical characterization.

Expected outputs: - Electronics architecture and BOM. - Firmware source
and build instructions. - Motor/encoder configuration and calibration
instructions. - Position-control demonstration. - Fault-handling test
results. - Controller schematic/PCB files if completed. - Electrical
test report.

### ACT-02 --- Mechanical: Design and Integration

Primary ownership: - Joint requirements and mechanical concept. - Motor
and gearbox fit evaluation in collaboration with ACT-01. - CAD models,
housing, mounting, output shaft, and bearing arrangement as needed. -
Output encoder mounting and alignment. - Fabrication drawings and
mechanical BOM. - Prototype fabrication and assembly. - Backlash,
repeatability, vibration/noise observations, and mechanical
characterization. - Assembly and maintenance documentation.

Expected outputs: - Mechanical specification. - CAD and assembly
files. - Engineering drawings. - Mechanical BOM. - Fabricated and
assembled rotary-joint prototype. - Encoder mounting design. -
Mechanical test report and assembly instructions.

### Shared responsibilities

Both interns must: - Agree on interfaces before ordering parts. - Review
motor, gearbox, encoder, and mounting compatibility together. - Keep
design decisions and revisions traceable. - Participate in design and
integration reviews. - Report measured results rather than unsupported
estimates. - Maintain reproducible build, assembly, and test
instructions. - Identify risks and escalate safety concerns promptly.

------------------------------------------------------------------------

## 6. Indicative 12-Week Plan

  -----------------------------------------------------------------------
  Week             Electronics       Mechanical         Shared checkpoint
                   workstream        workstream         
  ---------------- ----------------- ------------------ -----------------
  1                Review            Review actuator    Requirements
                   motor-control     mechanics and      draft
                   architecture and  joint use          
                   requirements                         

  2                Evaluate          Evaluate           Joint component
                   MCU/driver        motor/gearbox      shortlist
                   options           options            

  3                Bring up motor    Develop initial    Feasibility
                   and encoder       CAD concept        review

  4                Demonstrate       Complete           Interface review
                   controlled motor  housing/mounting   
                   operation         concept            

  5                Implement/adapt   Detail CAD and     Design review
                   FOC and           drawings           
                   measurements                         

  6                Demonstrate       Fabricate initial  First integration
                   closed-loop       mechanical parts   
                   position control                     

  7                Refine control    Assemble gearbox   Joint movement
                   and feedback      and output encoder demonstration

  8                Add diagnostics   Inspect alignment  Integrated
                   and defined fault and mechanical     prototype review
                   responses         operation          

  9                Develop host      Refine mechanical  Host-controlled
                   communication     design             actuator

  10               Evaluate custom   Characterize       Performance
                   PCB feasibility   backlash and       review
                                     repeatability      

  11               Run regression    Resolve mechanical Validation review
                   and fault tests   defects            

  12               Firmware release  CAD release and    Final
                   and report        report             demonstration and
                                                        handover
  -----------------------------------------------------------------------

This schedule assumes timely access to hardware and fabrication. If
custom PCB fabrication is delayed, a validated development-board
prototype takes precedence over an unfinished custom PCB.

------------------------------------------------------------------------

## 7. Requirements Must Be Frozen Before Procurement

The following are open decisions. Do not select a motor or gearbox based
only on price or physical size.

-   Intended joint and test fixture.
-   Required continuous and peak output torque.
-   Output speed and angular range.
-   Supply voltage and current limits.
-   Duty cycle and thermal limits.
-   Gear ratio, efficiency, backlash, and rated load.
-   Encoder type, resolution, and interface.
-   Supported control modes.
-   Communication interface and update rate.
-   Mechanical envelope and mounting pattern.
-   Test equipment and measurement method.
-   Target cost and what the target includes/excludes.

Create a requirements table with unique IDs, measurable acceptance
criteria, verification methods, owners, and evidence links. Any change
to an approved requirement should be recorded in a decision/change log.

### Units and reporting

Use SI units wherever possible: - Torque: N·m - Angular position: rad or
degrees, clearly identified - Angular velocity: rad/s or RPM, clearly
identified - Current: A - Voltage: V - Power: W - Temperature: °C -
Mass: kg - Dimensions: mm

Always distinguish **rated/continuous** values from **peak** values and
state the measurement conditions.

------------------------------------------------------------------------

## 8. Cost Planning

Preliminary targets from project planning:

  ---------------------------------------------------------------------
  Stage                                     Target Notes
  -------------------- --------------------------- --------------------
  A0 prototype                    ₹10,000--₹15,000 Development board
                                                   and basic bench
                                                   setup

  A1 smart actuator    ₹20,000--₹30,000 cumulative May include custom
                                                   PCB and improved
                                                   assembly
  ---------------------------------------------------------------------

These figures are planning allowances, not verified market prices.
Confirm current prices and availability before procurement. Clarify
whether taxes, shipping, fabrication, laboratory equipment, tools, and
rework are included.

Maintain an actual BOM with: - Manufacturer and exact part number. -
Vendor and quotation/link. - Unit price, quantity, and currency. - Taxes
and shipping where known. - Availability/lead time. - Revision or date
checked. - Alternatives and selection rationale.

A prototype BOM is not the same as a production cost model. Later
estimates must include assembly labour, test time, yield/rework,
tooling, warranty, and ongoing engineering.

------------------------------------------------------------------------

## 9. Open-Source Training References

These projects are references for learning and comparison, not
automatically approved components or designs for reuse. Review the
current repository state, hardware revision, license, limitations, and
validation evidence before adopting anything.

### Motor control and firmware

-   **SimpleFOC:** https://github.com/simplefoc/Arduino-FOC\
    Useful for learning motor-control concepts and evaluating a
    development path. Check supported drivers, MCU compatibility, sensor
    configuration, and limitations for the chosen hardware.

-   **moteus:** https://github.com/mjbots/moteus\
    Reference for integrated motor-controller architecture, firmware,
    communication, and diagnostics. Its hardware may exceed the
    voltage/current needs of the educational prototype.

-   **NautilusController:**
    https://github.com/JorgeMaker/NautilusController\
    Experimental controller reference. Verify current project status,
    implemented features, tests, and license before relying on it.

### Mechanical actuator design

-   **Shactuator / 3D-Printed Compliant Actuator:**
    https://github.com/shadmehr1/3D-Printed-Compliant-Actuator\
    Reference for mechanical design organization, transmission concepts,
    and characterization.

-   **Integrated Cycloidal Robotic Actuator:**
    https://github.com/AtomsClark/Integrated-Cycloidal-Robotic-Actuator\
    Experimental integrated actuator reference. Study its transmission
    and packaging, but do not assume it is lower cost or more suitable
    than a planetary gearbox.

### Commercial comparison references

-   **CubeMars:** https://www.cubemars.com/\
    Study integrated actuator packaging, motor/gearbox/controller
    integration, encoder placement, and published performance
    specifications.

-   **ODrive:** https://odriverobotics.com/\
    Reference for motor-control hardware and development workflows.
    Select a specific product only after checking motor, encoder,
    voltage, and current compatibility.

### Reuse and licensing

Before incorporating any external source code, PCB files, CAD, or
documentation: 1. Read the repository license and file-level notices. 2.
Record the source URL, commit/release or revision, and date reviewed. 3.
Preserve required copyright and license notices. 4. Identify third-party
dependencies and their licenses. 5. Ask for a review if the license is
unclear or incompatible with the intended distribution.

Do not assume that a public GitHub repository is automatically
open-source or that all files in it share the same license.

------------------------------------------------------------------------

## 10. Validation and Safety Principles

The first prototype is for controlled bench testing only.

Minimum engineering practices: - Use a suitable current-limited
low-voltage supply. - Secure the actuator to a fixture before applying
power. - Keep hands, clothing, and cables away from rotating parts. -
Establish safe startup, shutdown, and emergency-stop procedures. - Set
conservative current, speed, and travel limits. - Validate protective
behavior at low energy before increasing operating limits. - Test
communication loss and invalid commands under controlled conditions. -
Monitor temperature and stop tests if limits are exceeded. - Use
appropriate guards and test equipment for mechanical load testing. -
Record all test conditions and results.

Motor current alone cannot reliably distinguish collision from
acceleration, friction, or a mechanical jam. Do not describe current
monitoring as a complete collision-safety function.

A software stop command is not a substitute for a properly engineered
emergency-stop and power-isolation strategy. Human-interactive operation
requires a separate system-level safety assessment.

### Evidence required for each test

Record: - Test ID and requirement ID. - Hardware and firmware
revision. - Setup and instruments. - Supply voltage and current limit. -
Load and environmental conditions, where relevant. - Procedure and
expected result. - Measured result and pass/fail status. - Logs, plots,
photographs, or other evidence. - Tester and date. - Known limitations
or follow-up actions.

Never mark a requirement as passed without evidence.

------------------------------------------------------------------------

## 11. Suggested Repository Structure

``` text
kritva-actuator/
├── README.md
├── requirements/
│   ├── SYSTEM_REQUIREMENTS.md
│   ├── ACTUATOR_SPECIFICATION.md
│   └── SAFETY_REQUIREMENTS.md
├── planning/
│   └── v1/
│       ├── ROADMAP.md
│       ├── MILESTONE.md
│       ├── TASKS.md
│       └── ACCEPTANCE_CRITERIA.md
├── hardware/
│   ├── motor_controller/
│   ├── power_stage/
│   ├── sensing/
│   └── pcb/
├── mechanical/
│   ├── cad/
│   ├── gearbox/
│   └── assembly/
├── firmware/
│   ├── motor_control/
│   ├── foc/
│   ├── encoder/
│   ├── joint_control/
│   └── diagnostics/
├── communication/
│   └── can/
├── software/
│   └── kritva_driver/
├── tests/
│   ├── unit/
│   ├── hardware/
│   ├── performance/
│   └── safety/
└── docs/
    ├── architecture/
    ├── design/
    ├── bringup/
    └── validation/
```

This is a suggested structure; it can be adjusted to match the existing
KritvaOS repository conventions. Keep generated files, binaries, and
large CAD artifacts organized and versioned according to repository
policy.

------------------------------------------------------------------------

## 12. Definition of Done

A task is not complete merely because a design file or code change
exists.

A task is complete when: - Its acceptance criteria are met. - Relevant
tests have been executed. - Results and evidence are recorded. - CAD,
firmware, or documentation revisions are identifiable. - Limitations and
known defects are documented. - Required peer review is complete. - The
related requirement and task status are updated. - The change is
committed to version control using the project's commit conventions.

For hardware tasks, include the exact part number, board revision, and
test setup. For firmware tasks, include build instructions and test
results. For mechanical tasks, include CAD revision, drawings,
fabrication notes, and assembly checks.

------------------------------------------------------------------------

## 13. Final Expected Outcome

At the end of the initial project, the team should deliver:

1.  One low-voltage rotary actuator prototype on a secure bench fixture.
2.  A documented motor, gearbox, encoder, and controller configuration.
3.  Closed-loop position-control demonstration.
4.  Mechanical CAD, drawings, and assembly instructions.
5.  Firmware source, configuration, and build instructions.
6.  Measured performance and fault-test reports.
7.  Actual BOM and cost summary.
8.  Documented limitations and recommended next steps.
9.  A plan for A1 smart-actuator development and A2 KritvaOS
    integration.

The intended result is not simply a motor that rotates. It is a
measured, documented, maintainable prototype that provides a credible
foundation for a reusable Kritva smart actuator.

------------------------------------------------------------------------

## 14. Decision Log

Record decisions in a separate decision log or issue tracker. At
minimum, each decision should state: - Decision ID and date. -
Context/problem. - Options considered. - Decision and rationale. -
Impact on cost, performance, safety, and schedule. - Owner and review
status.

Initial planning choices: - Start with one low-voltage rotary joint. -
Buy the motor and gearbox initially. - Use an output-position encoder. -
Use a development board for A0. - Consider a custom controller PCB only
after initial validation. - Target CAN for the smart-actuator
integration stage. - Keep the first prototype on a controlled bench
fixture. - Treat budget and performance numbers as provisional until
requirements and supplier quotes are approved.

------------------------------------------------------------------------

**End of README**
